import json
import sys
from itertools import product
from pathlib import Path
from typing import Dict, Union

import typer

from test_with_deepimagej import write_test_summaries


def iterate_over_gh_matrix(matrix: Union[str, Dict[str, list]]):
    if isinstance(matrix, str):
        matrix = json.loads(matrix)

    assert isinstance(matrix, dict), matrix
    if "exclude" in matrix:
        raise NotImplementedError("matrix:exclude")

    elif "include" in matrix:
        if len(matrix) > 1:
            raise NotImplementedError("matrix:include with other keys")

        yield from matrix["include"]

    else:
        keys = list(matrix)
        for vals in product(*[matrix[k] for k in keys]):
            yield dict(zip(keys, vals))


def main(
    dist: Path,
    pending_matrix: str,
    fiji_path: Path,
    rdf_dir: Path = Path(__file__).parent / "../bioimageio-gh-pages/rdfs",
    postfix: str = "",
):
    """preliminary deepimagej check

    only checks if test outputs are obtained for Tensorflow 1 or torchscript weights .

    """
    print("Start tests")
    print(sys.argv[0]) # prints python_script.py
    print(sys.argv[1]) # prints var1
    print(sys.argv[2]) # prints var2
    print(sys.argv[3]) # prints var3

    summaries_dir = dist / "test_summaries"
    summaries_dir.mkdir(parents=True, exist_ok=True)
    for matrix in iterate_over_gh_matrix(pending_matrix):
        resource_id = matrix["resource_id"]
        print("Resource ID: ")
        print(resource_id)
        version_id = matrix["version_id"]
        print("Version ID: ")
        print(version_id)

        write_test_summaries(rdf_dir, resource_id, version_id, summaries_dir, fiji_path, postfix)


if __name__ == "__main__":
    typer.run(main)
