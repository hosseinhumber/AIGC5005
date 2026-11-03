from prepare_space import PACKAGES, requirements_text


def test_every_package_is_pinned_with_an_exact_version():
    lines = requirements_text().splitlines()
    assert len(lines) == len(PACKAGES)
    assert all("==" in line for line in lines)


def test_gradio_is_left_out_of_the_space_requirements():
    assert "gradio" not in requirements_text()
