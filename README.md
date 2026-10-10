# News topic modeling with LDA

Splits article text exports, removes metadata/punctuation/stopwords, plots n-grams, and fits 5/10/15/20-topic Gensim LDA models.

## Setup and execution

Use Python 3.11 and a separate virtual environment for this project. Run commands from this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python check_inputs.py
python -m jupyterlab
```

On Windows, activate with `.venv\Scripts\activate`. For notebooks, select this environment’s kernel and execute from the top in a fresh kernel. The first code cell exposes `INPUT_PATHS` where old machine-specific paths existed. `PROJECT_DATA_DIR` changes the base for those configured paths; remaining relative paths use the notebook working directory.

## Notebooks

- [index.ipynb](index.ipynb)

## Inputs

Supply these inputs yourself; no dataset is downloaded automatically:

- `DataDictionary/Articles/*.txt`

## Outputs

Word-cloud/ngram plots and lda_output HTML visualizations/topic summaries.

## Implementation and limitations

Article files are user-supplied UTF-8 text. Install NLTK stopwords, punkt, and punkt_tab resources explicitly before execution. The parser preserves the original document-marker pattern. Bundled HTML/PNG files are historical outputs; generated HTML includes browser JavaScript. Do not treat inferred topics as ground-truth labels.

Reusable model/analysis functions live in `experiment_index.py`. Notebooks retain the experiment sequence, training, and visual narrative.

Install language resources explicitly with `python -m nltk.downloader stopwords punkt punkt_tab`.

## Verification

The workspace regression suite checks source/notebook validity and selected behavior with bundled or synthetic inputs. Full experiment training and historical metric reproduction are not implied. See the workspace `REFACTOR_REPORT.md` for exact test coverage and unresolved runtime requirements.

## Outstanding dependency advisory

The audited NLTK 3.10.3 dependency has [CVE-2026-81726](https://github.com/advisories/GHSA-8mgp-746c-j5xp), with no published patched release at the time of review. This workflow uses stopwords and tokenization, not the affected parser/tagger model-artifact APIs. This limits applicability but does not make the package vulnerability-free; do not use this environment to run untrusted model-loading workflows. Re-audit before deploying or upgrading.
