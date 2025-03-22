import unittest
from markdown_blocks import BlockType, block_to_block_type

class TestMarkdownBlocks(unittest.TestCase):
    def test_to_type_paragraph(self):
        block1 = "My names Randy.\nI like cheese."
        block2 = "I like long walks on the beach and playing poker with my friends."
        block3 = "Hello\n- there\n1. how\n## how\n```are```\nyou\ndoing"
        type1 = block_to_block_type(block1)
        type2 = block_to_block_type(block2)
        type3 = block_to_block_type(block3)

        self.assertTupleEqual(
            (BlockType.PARAGRAPH, BlockType.PARAGRAPH, BlockType.PARAGRAPH),
            (type1, type2, type3)
        )

    def test_to_type_heading(self):
        block1 = "# i am a LARGE heading"
        block2 = "i'm not a heading"
        block3 = "#### i'm a small heading"
        block4 = "######## i'm not a heading"
        type1 = block_to_block_type(block1)
        type2 = block_to_block_type(block2)
        type3 = block_to_block_type(block3)
        type4 = block_to_block_type(block4)
        self.assertTupleEqual(
            (BlockType.HEADING, BlockType.PARAGRAPH, BlockType.HEADING, BlockType.PARAGRAPH),
            (type1, type2, type3, type4)
        )

    def test_to_type_code(self):
        block1 = "``i'm not code :(```"
        block2 = "```i'm not code again :("
        block3 = "`\n``i'm not code!```"
        block4 = "```i'm code```"
        block5 = "```my\ncode\nis\ncool```"
        type1 = block_to_block_type(block1)
        type2 = block_to_block_type(block2)
        type3 = block_to_block_type(block3)
        type4 = block_to_block_type(block4)
        type5 = block_to_block_type(block5)
        self.assertTupleEqual(
            (BlockType.PARAGRAPH, BlockType.PARAGRAPH, BlockType.PARAGRAPH, BlockType.CODE, BlockType.CODE),
            (type1, type2, type3, type4, type5)
        )

    def test_to_type_quote(self):
        block1 = "> 'richard feynman once said'"
        block2 = ">i'm no quote"
        block3 = "i'm a paragraph"
        block4 = "> back to feynman\n> so, basically\n> he was cool"
        block5 = "> with the energy that i\nwant it want it\n> i want it!"
        type1 = block_to_block_type(block1)
        type2 = block_to_block_type(block2)
        type3 = block_to_block_type(block3)
        type4 = block_to_block_type(block4)
        type5 = block_to_block_type(block5)
        self.assertTupleEqual(
            (BlockType.QUOTE, BlockType.PARAGRAPH, BlockType.PARAGRAPH, BlockType.QUOTE, BlockType.PARAGRAPH),
            (type1, type2, type3, type4, type5)
        )

    def test_to_type_unordered(self):
        block1 = "- tacos\n- eggs\n- dollars\n- cool"
        block2 = "- hi"
        block3 = "- not\n- an\nunordered"
        block4 = "you know me\n- i'm the rock"
        block5 = "-hello\n- i'm a list just like you.. totally"
        type1 = block_to_block_type(block1)
        type2 = block_to_block_type(block2)
        type3 = block_to_block_type(block3)
        type4 = block_to_block_type(block4)
        type5 = block_to_block_type(block5)
        self.assertTupleEqual(
            (BlockType.UNORDERED_LIST, BlockType.UNORDERED_LIST, BlockType.PARAGRAPH, BlockType.PARAGRAPH, BlockType.PARAGRAPH),
            (type1, type2, type3, type4, type5)
        )

    def test_to_type_ordered(self):
        block1 = "- i'm unordered\n- but im still a list just like you.."
        block2 = "1. bacon\n2. cheese\n3. pizza\n4. eggs"
        block3 = "2. oh no i start at two\n3. and go up"
        block4 = "1. hi i'm a list\n3. you don't believe me?"
        block5 = "1. sing with me\n2. sing for the year"
        type1 = block_to_block_type(block1)
        type2 = block_to_block_type(block2)
        type3 = block_to_block_type(block3)
        type4 = block_to_block_type(block4)
        type5 = block_to_block_type(block5)
        self.assertTupleEqual(
            (BlockType.UNORDERED_LIST, BlockType.ORDERED_LIST, BlockType.PARAGRAPH, BlockType.PARAGRAPH, BlockType.ORDERED_LIST),
            (type1, type2, type3, type4, type5)
        )

if __name__ == "__main__":
    unittest.main()