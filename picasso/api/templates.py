class BasicTemplate:

    def __init__(self, barcode_horizontal_direction, barcode_vertical_direction,
                 print_map):

        if barcode_horizontal_direction == 'right':
            self.barcode_horizontal_direction = 'right'
        else:
            self.barcode_horizontal_direction = 'left'

        if barcode_vertical_direction in ['top', 'middle', 'botton']:
            self.barcode_vertical_direction = barcode_vertical_direction
        else:
            self.barcode_vertical_direction = 'middle'

        if print_map:
            self.map = True
        else:
            self.map = False


class TemplateTopBackground(BasicTemplate):
    def __init__(self, barcode_horizontal_direction, barcode_vertical_direction,
                 print_map, background_image):
        BasicTemplate.__init__(self, barcode_horizontal_direction, barcode_vertical_direction,
                               print_map)
        self.background_image = background_image


class TemplateWithHeaderAndFooter(BasicTemplate):
    def __init__(self, barcode_horizontal_direction, barcode_vertical_direction,
                 print_map, header_image, footer_image):
        BasicTemplate.__init__(self, barcode_horizontal_direction, barcode_vertical_direction,
                               print_map)
        self.background_image = header_image
        self.footer_image = footer_image
