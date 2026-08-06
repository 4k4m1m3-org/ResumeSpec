from pathlib import Path
import xml.etree.ElementTree as ET


ROOT = Path(__file__).parent.parent


def test_minimal_xml_example_is_valid():
    file = ROOT / "examples/xml/minimal.xml"

    tree = ET.parse(file)
    root = tree.getroot()

    assert root.tag == "resumeSpec"