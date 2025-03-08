# dbt-tidy

`dbt-tidy` is a CLI tool written in Python and is designed to run `sweeps` (checks) against the structure and quality of your dbt project. It ensures that your project adheres to best practices and consistency standards, helping maintain clean and efficient dbt codebases.

The `sweeps` in this package are inspired by `dbt-project-evaluator` and `dbt-checkpoint`, but it sets itself apart by offering a more flexible and easily extendable framework for creating custom `sweeps`.

## Installation

Use the package manager [pip](https://pypi.org/project/dbt-tidy/) to install `dbt-tidy`.

```bash
pip install dbt-tidy
```

## Usage

```bash
#Run all built-in and custom sweeps
dbt-tidy sweep

Sweeping...

Duplicate Sources
Status: pass

Direct Join to Source
Status: fail
Resolution: Read from the staging model instead of the source.
Nodes:
  - model.your_package.node_one
  - model.your_package.node_two
  - model.your_package.node_three
  - model.your_package.node_four
  - model.your_package.node_five
  ...and 5 more
```

```bash
#Use the --sweeps options to run a subset of sweeps

dbt-tidy sweep --sweeps root_models duplicate_sources
```

```bash
#Use the --output-failures to write failures to a JSON file.

dbt-tidy sweep --output-failures ./failures.json
```

```bash
#Use the --manifest-path to specify the location of your dbt manifest.
#If this is not specified, dbt-tidy will assume it is at: target/manifest.json

dbt-tidy sweep --manifest-path ./located/here/manifest.json
```

## Configuration
You can configure the behavior of `dbt-tidy` by creating a `tidy.yaml` file in your project root. In this file, you can specify which sweeps to enable or exclude and set project-specific settings.

```yaml
manifest_path: some/directory/manifest.json

#The directory where your custom sweeps are located.
custom_sweeps_path: .tidy

#Control the behavior of the `sweeps` list.
#`include`: Only run the specified sweeps.
#`exclude`: Run all sweeps, except those specified.
#`all`: Run all sweeps, regardless of what is defined in the sweeps list.
#NOTE: The --sweeps cli option will always override what is specified in this file.
mode: include
sweeps:
  - root_models
```

## Writing Custom Sweeps
If you would like to create custom sweeps for your project, `dbt-tidy` allows you to write and integrate them easily.

It is as easy as:
1.	Create a directory for your sweeps. By default, `dbt-tidy` will look for custom sweeps in `./.tidy`, but you can override this in the `tidy.yaml` file.
2.	Create a `sweep` decorated function which returns a list of dbt unique ids.

The `@sweep` decorator not only runs validation checks but also provides a fully parsed manifest of your dbt project, represented as a Pydantic model. This means you have direct access to the entire dbt manifest, including models, tests, and other configurations, in a structured and type-validated format. The power of this approach lies in how easily you can interact with and query the project metadata, enabling you to write more sophisticated custom `sweeps`.

```python
from tidy.sweeps.base import sweep
from tidy.manifest.utils.types import ManifestType


@sweep(
    name="Friendly Name That Will Print in the CLI",
    resolution="Optionally provide a brief explanation for how to correct failures.",
)
def no_ephemerals(manifest: ManifestType) -> list:
    failures = []
    for node in manifest.nodes.values():
        if node.resource_type == "model" and node.config.materialized == "ephemeral":
            failures.append(node.unique_id)

    return failures

```

Then you can run this custom `sweep` the same as any built-in `sweep`.
```bash
#Run all built-in and custom sweeps
dbt-tidy sweep --sweeps no_ephemerals

Sweeping...

Friendly Name That Will Print in the CLI
Status: pass
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

MIT License

Copyright (c) 2025 Cameron Cyr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.