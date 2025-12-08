# presidio_anonymizer/services/custom_operators.py

from presidio_anonymizer.operators import Operator


class GenZOperator(Operator):
    """
    Example Gen-Z anonymizer operator.

    Replace PERSON names and PHONE_NUMBERs with fun Gen-Z style replacements.
    """

    def anonymize(self, text: str, analyzer_result=None):
        """Replace recognized entities with Gen-Z style replacements."""
        # Simple example replacement
        if analyzer_result and analyzer_result.entity_type == "PERSON":
            return "💀"  # Example replacement for names
        if analyzer_result and analyzer_result.entity_type == "PHONE_NUMBER":
            return "📱"  # Example replacement for phone numbers
        return text
