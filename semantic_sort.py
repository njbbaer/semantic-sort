import spacy
import numpy as np
import argparse
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedSeq
from scipy.cluster.hierarchy import linkage, leaves_list
from scipy.spatial.distance import pdist

yaml = YAML()


def semantic_sort(words):
    nlp = spacy.load("en_core_web_lg")

    words_nlp = [(w, nlp(w)[0]) for w in words]
    unknown_words = [w for w, t in words_nlp if not t.has_vector]

    valid = [(w, t.vector) for w, t in words_nlp if t.has_vector]
    vectors = np.array([v for _, v in valid])
    order = leaves_list(linkage(pdist(vectors, "cosine"), "ward"))

    return [valid[i][0] for i in order], unknown_words


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sort words semantically based on word embeddings"
    )
    parser.add_argument("input", help="Input YAML file containing words to sort")
    parser.add_argument(
        "-o",
        "--output",
        help="Output YAML file (default: output.yml)",
        default="output.yml",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    with open(args.input, "r") as f:
        words = yaml.load(f)

    sorted_words, unknown_words = semantic_sort(words)

    output_yaml = {
        "sorted_words": CommentedSeq(sorted_words),
        "unknown_words": unknown_words,
    }
    output_yaml["sorted_words"].fa.set_flow_style()
    with open(args.output, "w") as f:
        yaml.dump(output_yaml, f)


if __name__ == "__main__":
    main()
