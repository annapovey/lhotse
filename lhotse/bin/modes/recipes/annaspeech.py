from typing import List

import click

from lhotse.bin.modes import download, prepare
from lhotse.recipes.annaspeech import prepare_annaspeech
from lhotse.utils import Pathlike


@prepare.command(context_settings=dict(show_default=True))
@click.argument("corpus_dir", type=click.Path(exists=True, dir_okay=True))
@click.argument("output_dir", type=click.Path())
@click.option(
    "-s",
    "--split",
    default=["dev", "test", "small"],
    multiple=True,
    help="Splits to prepare (available options: train, dev, test, validated, invalidated, other)",
)
@click.option(
    "-j",
    "--num-jobs",
    type=int,
    default=1,
    help="How many threads to use (can give good speed-ups with slow disks).",
)
@click.option(
    "-d",
    "--dataset",
    type=str,
    default="annaspeech",
    help="What is sataset name.",
)
def annaspeech(
    corpus_dir: Pathlike,
    output_dir: Pathlike,
    split: List[str],
    num_jobs: int,
    dataset: str,
):
    """
    Mozilla CommonVoice manifest preparation script.
    CORPUS_DIR is expected to contain sub-directories that are named with CommonVoice language codes,
    e.g., "en", "pl", etc.
    """
    # languages = language[0] if len(language) == 1 else language
    prepare_annaspeech(
        corpus_dir=corpus_dir,
        splits=split,
        output_dir=output_dir,
        num_jobs=num_jobs,
        dataset=dataset,
    )
