import pytest
from transformers import AutoTokenizer

from finetune import MODEL
from review_data import load_reviews


@pytest.fixture(scope="session")
def tokenizer():
    return AutoTokenizer.from_pretrained(MODEL)


@pytest.fixture(scope="session")
def reviews():
    return load_reviews()
