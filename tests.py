import unittest
from core.utils import exclude_tagged_text

class TestExcludeTaggedText(unittest.TestCase):
    def test_exclude_tagged_text(self):
        self.assertEqual(
            exclude_tagged_text("This is a test.", None),
            "This is a test."
        )
        self.assertEqual(
            exclude_tagged_text(
                "This <test>hallelujah</test> is a test to check if "
                "<test>ahaala</test> works as expected.",
                "test"
            ),
            "This is a test to check if works as expected."
        )
        self.assertEqual(
            exclude_tagged_text(
                "This is a test to check if "
                "exclusion works as expected.",
                "think"
            ),
            "This is a test to check if exclusion works as expected."
        )
        self.assertEqual(
            exclude_tagged_text(
                "This is a <test>test</test> to check if "
                "<test>exclusion</test> works as expected.",
                "think"
            ),
            "This is a <test>test</test> to check if <test>exclusion</test> works as expected."
        )


if __name__ == '__main__':
    unittest.main()

