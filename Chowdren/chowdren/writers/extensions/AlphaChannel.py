from chowdren.writers.objects import ObjectWriter

from chowdren.common import (get_image_name, get_animation_name, to_c,
    make_color)

from chowdren.writers.events import (ComparisonWriter, ActionMethodWriter,
    ConditionMethodWriter, ExpressionMethodWriter, make_table, EmptyAction)

class AlphaImageObject(ObjectWriter):
    class_name = 'AlphaImageObject'
    includes = ['objects/alphaimage.h']

    def write_init(self, writer):
        pass

actions = make_table(ActionMethodWriter, {
    32 : 'blend_color.set_alpha',
})

conditions = make_table(ConditionMethodWriter, {
})

expressions = make_table(ExpressionMethodWriter, {
    15 : '.blend_color.a'
})

def get_object():
    return AlphaImageObject
