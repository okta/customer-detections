import os
import yaml
import pytest
import yamllint.config
import yamllint.linter
from glob import glob

BASE_DIR = os.path.dirname(__file__)
RULE_DIRS = [
    os.path.join(BASE_DIR, "..", "detections"),
    os.path.join(BASE_DIR, "..", "hunts"),
]


def list_yaml_files():
    """Yield all .yml and .yaml files from rule directories (normalized paths)."""
    yaml_files = []
    for rule_dir in RULE_DIRS:
        # Resolve the directory path cleanly (removes 'tests/../')
        clean_dir = os.path.abspath(rule_dir)
        
        if not os.path.exists(clean_dir):
            print(f"WARNING: Directory not found: {clean_dir}")
            continue

        # Find files and ensure they are absolute/clean paths
        found = glob(os.path.join(clean_dir, "*.yml")) + \
                glob(os.path.join(clean_dir, "*.yaml"))
                
        yaml_files.extend([os.path.abspath(f) for f in found])

    return sorted(yaml_files)


def load_yaml_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# -------- YAML PARSING TEST ---------

@pytest.mark.parametrize("yaml_file", list_yaml_files())
def test_yaml_parses(yaml_file):
    """Ensure every YAML rule parses successfully."""
    try:
        data = load_yaml_file(yaml_file)
        assert isinstance(data, dict), f"YAML must be a dict in {yaml_file}"
    except Exception as e:
        pytest.fail(f"Failed to parse {yaml_file}: {e}")


# -------- REQUIRED FIELD VALIDATION ---------

REQUIRED_FIELDS = [
    "title",
    "id",
    "description",
    "author",
    "threat",
    "created_date",
    "modified_date",
    "prevention",
    "detection",
    "false_positives",
]

@pytest.mark.parametrize("yaml_file", list_yaml_files())
def test_required_fields(yaml_file):
    data = load_yaml_file(yaml_file)
    missing = [field for field in REQUIRED_FIELDS if field not in data]

    if missing:
        pytest.fail(
            f"Missing required fields in {yaml_file}: {', '.join(missing)}"
        )


# -------- UNIQUE ID VALIDATION ---------

def test_unique_ids():
    """Ensure IDs are globally unique across detections + hunts."""
    seen_ids = {}
    for yaml_file in list_yaml_files():
        data = load_yaml_file(yaml_file)
        rule_id = data.get("id")

        if rule_id in seen_ids:
            pytest.fail(
                f"Duplicate ID '{rule_id}' found in:\n"
                f" - {seen_ids[rule_id]}\n"
                f" - {yaml_file}"
            )

        seen_ids[rule_id] = yaml_file


# -------- DETECTION BLOCK VALIDATION ---------

@pytest.mark.parametrize("yaml_file", list_yaml_files())
def test_detection_block(yaml_file):
    """Ensure detection block exists and contains at least one query."""
    data = load_yaml_file(yaml_file)
    detection = data.get("detection")

    assert isinstance(detection, dict), f"detection must be a dict in {yaml_file}"
    assert len(detection) >= 1, f"No detection queries found in {yaml_file}"


# -------- YAMLLINT VALIDATION ---------

@pytest.mark.parametrize("yaml_file", list_yaml_files())
def test_yamllint_compliance(yaml_file):
    """Run yamllint on a single file using the project's .yamllint config."""
    
    # 1. Force the correct path to .yamllint
    # We go up two levels from this test file (tests/ -> repo_root/)
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    config_path = os.path.join(repo_root, ".yamllint")
    
    # SAFETY CHECK: Fail if config is missing
    if not os.path.exists(config_path):
        pytest.fail(f"Config not found at: {config_path}")

    # 2. Load the config
    # We print the path so you can see it in pytest output (use -s)
    print(f"DEBUG: Using config from {config_path}")
    conf = yamllint.config.YamlLintConfig(file=config_path)

    # 3. Read the file content
    with open(yaml_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 4. RUN THE LINTER (Wrapped in list() to force execution!)
    problems = list(yamllint.linter.run(content, conf, yaml_file))

    # 5. Fail if any errors found
    if problems:
        error_msg = f"Yamllint violations in {os.path.basename(yaml_file)}:\n"
        for p in problems:
            error_msg += (
                f"  Line {p.line}: [{p.level.upper()}] {p.message} ({p.rule})\n"
            )
        pytest.fail(error_msg)