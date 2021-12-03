"""Created by Jhesed Tacadena Dec 08, 2020."""

IS_COVID_19 = True
IS_VACCINE_AVAILABLE = True


def is_wfh() -> bool:
    """A very useless function that will always return WFH."""
    if IS_COVID_19 and not IS_VACCINE_AVAILABLE:
        return True

    if IS_VACCINE_AVAILABLE:
        # Still return True, lols
        return True

    # Return True regardless. lols
    return True


if __name__ == "__main__":
    print(is_wfh())
