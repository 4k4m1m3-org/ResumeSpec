# Parser

The parser loads documents into a `ResumeProfile`.

## API

- `parse(path)`
- `parse_data(data)`
- `parse_yaml(path)`
- `parse_xml(path)`

## Behavior

- JSON is parsed as the canonical format.
- YAML and XML are parsed as secondary formats.
- Parsing is separate from validation.
- XML parsing uses `defusedxml` for safety.

## Result

The parser returns a `ResumeProfile` with:

- `data`
- `metadata`
- `sections`

