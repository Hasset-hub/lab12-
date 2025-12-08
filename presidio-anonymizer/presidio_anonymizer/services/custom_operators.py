# presidio_anonymizer/services/custom_operators.py

from presidio_anonymizer.operators import Operator

class GenZOperator(Operator):
    """
    Example Gen-Z anonymizer operator.
    Replace PERSON names and PHONE_NUMBERs with fun Gen-Z style replacements.
    """

    def anonymize(self, text: str, analyzer_result=None):
        # Simple example replacement
        if analyzer_result and analyzer_result.entity_type == "PERSON":
            return "GOAT"
        elif analyzer_result and analyzer_result.entity_type == "PHONE_NUMBER":
            return "vibe check"
        return text
