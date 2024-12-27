# semantic-sort

The `semantic-sort` tool uses embeddings to group a list of words by semantic similarity. Similar words appear closer together in the output.

I found this useful for a language model character prompting technique that provides the model a list of character adjectives to simulate. Sorting the words in a coherent way appears to help the model absorb a greater number of adjectives effectively.

## Install

```bash
pipenv install
pipenv run python -m spacy download en_core_web_lg
```

## Usage

```bash
pipenv run python semantic_sort.py example.yml
```

Input file should contain a YAML list of words. Output will be sorted with related words grouped together.

`example.yml`:

```yaml
[yellow, seafoam, magenta, lemon, maroon, salmon, ivory, rose, fuchsia,
mint, azure, emerald, violet, crimson, navy, scarlet, sage, black, khaki, aqua,
gold, ruby, cobalt, white, peach, wine, cerulean, purple, tangerine, green, mauve,
tan, burgundy, brown, periwinkle, teal, beige, indigo, orange, amber, plum, pink,
lime, olive, jade, silver, turquoise, red, forest, coral, blue, gray]
```

`output.yml`:

```yaml
sorted_words: [tangerine, peach, plum, sage, mint, olive, lemon, lime, forest, salmon,
  wine, navy, khaki, ivory, maroon, burgundy, beige, purple, pink, green, orange,
  yellow, red, blue, tan, black, white, brown, gray, ruby, amber, jade, rose, cobalt,
  gold, silver, azure, cerulean, coral, emerald, turquoise, periwinkle, teal, fuchsia,
  mauve, seafoam, aqua, crimson, scarlet, indigo, magenta, violet]
unknown_words: []
```
