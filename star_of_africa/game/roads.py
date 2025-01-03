import pygame
from pygame.sprite import Group, Sprite


class Path(Sprite):

    COLOR = (255, 0, 0, 255)

    def __init__(
        self,
        id: int,
        x: float,
        y: float,
        links: list[int] = None,
        radius: float = 5,
        width: int = 2,
        visible: bool = False,
        groups: Group | list[Group] = None,
    ):
        super().__init__()
        self.id = id
        self.x = x
        self.y = y
        self.links = links if links else []
        self.radius = radius
        self.width = width
        self.visible = visible
        self.surface = self._create_surface(visible)

    def _create_surface(self, visible: bool) -> pygame.Surface:
        surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        surface.fill((0, 0, 0, 0))
        color = self.COLOR if visible else (0, 0, 0, 0)
        pygame.draw.circle(
            surface, color, (self.radius, self.radius), self.radius, self.width
        )
        return surface

    def display(self, screen: pygame.Surface, resolution) -> None:
        x = self.x * resolution[0] - self.radius
        y = self.y * resolution[1] - self.radius
        # screen.blit(self.surface, (x, y))
        font = pygame.font.SysFont("arial", 12)
        text = font.render(str(self.id), True, (0, 0, 0))
        screen.blit(text, (x, y))

        for link in self.links:
            node = [path for path in self.groups()[0].sprites() if path.id == link][0]
            pygame.draw.line(
                screen,
                self.COLOR,
                (self.x * resolution[0], self.y * resolution[1]),
                (node.x * resolution[0], node.y * resolution[1]),
                self.width,
            )


ROADS = Group(
    [
        Path(1, 0.496, 0.873, links=[2]),
        Path(2, 0.486, 0.827, links=[1, 3]),
        Path(3, 0.498, 0.802, links=[2, 4]),
        Path(4, 0.487, 0.778, links=[3, 5]),
        Path(5, 0.448, 0.757, links=[4, 6]),
        Path(6, 0.487, 0.738, links=[5, 7]),
        Path(7, 0.521, 0.731, links=[6, 8]),
        Path(8, 0.554, 0.734, links=[7, 9]),
        Path(9, 0.604, 0.722, links=[8, 10, 15]),
        Path(10, 0.605, 0.763, links=[9, 11]),
        Path(11, 0.604, 0.792, links=[10, 12]),
        Path(12, 0.655, 0.791, links=[11, 13]),
        Path(13, 0.677, 0.754, links=[12, 14]),
        Path(14, 0.686, 0.733, links=[13, 15]),
        Path(15, 0.657, 0.721, links=[9, 14]),
        Path(16, 0.704, 0.717, links=[14, 17, 39]),
        Path(17, 0.67, 0.706, links=[16, 18]),
        Path(18, 0.639, 0.692, links=[17, 19]),
        Path(19, 0.605, 0.677, links=[18, 20]),
        Path(20, 0.571, 0.671, links=[19, 21]),
        Path(21, 0.536, 0.668, links=[20, 22]),
        Path(22, 0.5, 0.671, links=[21, 23]),
        Path(23, 0.463, 0.663, links=[22, 24]),
        Path(24, 0.427, 0.631, links=[23, 25]),
        Path(25, 0.479, 0.647, links=[24, 26]),
        Path(26, 0.511, 0.639, links=[25, 27]),
        Path(27, 0.536, 0.622, links=[26, 28]),
        Path(28, 0.579, 0.61, links=[27, 29]),
        Path(29, 0.627, 0.587, links=[28, 30]),
        Path(30, 0.641, 0.563, links=[29, 31]),
        Path(31, 0.661, 0.544, links=[30, 32]),
        Path(32, 0.713, 0.534, links=[31, 33, 51]),
        Path(33, 0.734, 0.565, links=[32, 34]),
        Path(34, 0.723, 0.594, links=[33, 35]),
        Path(35, 0.723, 0.62, links=[34, 36]),
        Path(36, 0.752, 0.638, links=[35, 37, 41]),
        Path(37, 0.764, 0.655, links=[36, 38]),
        Path(38, 0.773, 0.687, links=[37, 39]),
        Path(39, 0.723, 0.7, links=[38, 16]),
        Path(40, 0.764, 0.603, links=[36, 41]),
        Path(41, 0.779, 0.562, links=[40, 42]),
        Path(42, 0.798, 0.54, links=[41, 43]),
        Path(43, 0.825, 0.52, links=[42, 44]),
        Path(44, 0.857, 0.504, links=[43, 45]),
        Path(45, 0.887, 0.487, links=[44, 46]),
        Path(46, 0.918, 0.454, links=[45, 47]),
        Path(47, 0.87, 0.467, links=[46, 48]),
        Path(48, 0.838, 0.467, links=[47, 49]),
        Path(49, 0.78, 0.468, links=[48, 50, 69]),
        Path(50, 0.766, 0.497, links=[49, 51]),
        Path(51, 0.739, 0.509, links=[32, 50]),
        Path(52, 0.457, 0.598, links=[24, 53]),
        Path(53, 0.454, 0.571, links=[52, 54]),
        Path(54, 0.454, 0.529, links=[53, 55]),
        Path(55, 0.459, 0.492, links=[54, 56]),
        Path(56, 0.466, 0.468, links=[55, 57, 70, 113]),
        Path(57, 0.493, 0.455, links=[56, 58]),
        Path(58, 0.521, 0.448, links=[57, 59]),
        Path(59, 0.552, 0.442, links=[58, 60]),
        Path(60, 0.593, 0.429, links=[59, 61, 106, 107]),
        Path(61, 0.63, 0.446, links=[60, 62]),
        Path(62, 0.641, 0.48, links=[61, 63]),
        Path(63, 0.668, 0.513, links=[32, 62]),
        Path(64, 0.648, 0.422, links=[60, 65]),
        Path(65, 0.684, 0.413, links=[64, 66]),
        Path(66, 0.718, 0.402, links=[65, 67]),
        Path(67, 0.757, 0.374, links=[66, 68]),
        Path(68, 0.761, 0.406, links=[67, 69]),
        Path(69, 0.771, 0.433, links=[49, 68]),
        Path(70, 0.436, 0.471, links=[56, 71]),
        Path(71, 0.4, 0.471, links=[70, 72]),
        Path(72, 0.354, 0.488, links=[71, 73]),
        Path(73, 0.352, 0.45, links=[72, 74]),
        Path(74, 0.354, 0.429, links=[73, 75]),
        Path(75, 0.338, 0.406, links=[74, 76]),
        Path(76, 0.318, 0.389, links=[75, 77]),
        Path(77, 0.273, 0.364, links=[76, 78]),
        Path(78, 0.255, 0.401, links=[77, 79]),
        Path(79, 0.229, 0.422, links=[78, 80, 140]),
        Path(80, 0.202, 0.427, links=[79, 81]),
        Path(81, 0.171, 0.444, links=[80, 82]),
        Path(82, 0.121, 0.447, links=[81, 83]),
        Path(83, 0.159, 0.425, links=[82, 84]),
        Path(84, 0.157, 0.399, links=[83, 85]),
        Path(85, 0.129, 0.386, links=[84, 86]),
        Path(86, 0.073, 0.373, links=[85, 87]),
        Path(87, 0.111, 0.352, links=[86, 88]),
        Path(88, 0.138, 0.339, links=[87, 89]),
        Path(89, 0.177, 0.344, links=[88, 90]),
        Path(90, 0.202, 0.328, links=[89, 91]),
        Path(91, 0.225, 0.306, links=[90, 92]),
        Path(92, 0.25, 0.284, links=[91, 93]),
        Path(93, 0.252, 0.261, links=[92, 94]),
        Path(94, 0.209, 0.229, links=[93, 95]),
        Path(95, 0.252, 0.221, links=[94, 96, 114]),
        Path(96, 0.271, 0.231, links=[95, 97]),
        Path(97, 0.296, 0.246, links=[96, 98]),
        Path(98, 0.316, 0.272, links=[97, 99]),
        Path(99, 0.359, 0.29, links=[98, 100]),
        Path(100, 0.412, 0.303, links=[99, 101]),
        Path(101, 0.452, 0.312, links=[100, 102]),
        Path(102, 0.48, 0.327, links=[101, 103]),
        Path(103, 0.504, 0.343, links=[102, 104]),
        Path(104, 0.53, 0.357, links=[103, 105]),
        Path(105, 0.552, 0.376, links=[104, 106]),
        Path(106, 0.562, 0.399, links=[60, 105]),
        Path(107, 0.552, 0.419, links=[60, 108]),
        Path(108, 0.529, 0.407, links=[107, 109]),
        Path(109, 0.512, 0.389, links=[108, 110]),
        Path(110, 0.471, 0.374, links=[109, 111]),
        Path(111, 0.454, 0.403, links=[110, 112]),
        Path(112, 0.448, 0.426, links=[111, 113]),
        Path(113, 0.454, 0.447, links=[56, 112]),
        Path(114, 0.255, 0.146, links=[95, 115]),
        Path(115, 0.279, 0.209, links=[114, 116]),
        Path(116, 0.311, 0.222, links=[115, 117]),
        Path(117, 0.35, 0.224, links=[116, 118]),
        Path(118, 0.386, 0.208, links=[117, 119]),
        Path(119, 0.434, 0.188, links=[118, 120]),
        Path(120, 0.421, 0.226, links=[119, 121]),
        Path(121, 0.436, 0.245, links=[120, 122]),
        Path(122, 0.475, 0.239, links=[121, 123]),
        Path(123, 0.475, 0.283, links=[122, 124]),
        Path(124, 0.504, 0.299, links=[123, 125]),
        Path(125, 0.539, 0.302, links=[124, 126]),
        Path(126, 0.571, 0.298, links=[125, 127]),
        Path(127, 0.605, 0.307, links=[126, 128]),
        Path(128, 0.634, 0.332, links=[127, 129, 131]),
        Path(129, 0.634, 0.37, links=[128, 130]),
        Path(130, 0.618, 0.39, links=[60, 129]),
        Path(131, 0.639, 0.303, links=[128, 132]),
        Path(132, 0.646, 0.284, links=[131, 133]),
        Path(133, 0.666, 0.27, links=[132, 134]),
        Path(134, 0.661, 0.226, links=[133]),
        Path(135, 0.807, 0.804, links=[136]),
        Path(136, 0.838, 0.776, links=[135, 137]),
        Path(137, 0.843, 0.753, links=[136, 138]),
        Path(138, 0.843, 0.73, links=[137, 139]),
        Path(139, 0.887, 0.718, links=[138]),
        Path(140, 0.232, 0.443, links=[79, 141]),
        Path(141, 0.252, 0.476, links=[140]),
    ]
)

BOATS = Group(
    [
        Path(1, 0.495, 0.872, links=[2, 64]),
        Path(2, 0.445, 0.86, links=[1, 3]),
        Path(3, 0.416, 0.843, links=[2, 4]),
        Path(4, 0.377, 0.851, links=[3, 5]),
        Path(5, 0.32, 0.848, links=[4, 6]),
        Path(6, 0.271, 0.829, links=[5, 7]),
        Path(7, 0.245, 0.804, links=[6, 8]),
        Path(8, 0.227, 0.776, links=[7, 9]),
        Path(9, 0.218, 0.749, links=[8, 10]),
        Path(10, 0.207, 0.717, links=[9, 11]),
        Path(11, 0.198, 0.676, links=[10, 12]),
        Path(12, 0.148, 0.635, links=[11, 13]),
        Path(13, 0.125, 0.607, links=[12, 14]),
        Path(14, 0.105, 0.582, links=[13, 15]),
        Path(15, 0.089, 0.553, links=[14, 16]),
        Path(16, 0.079, 0.521, links=[15, 17]),
        Path(17, 0.068, 0.493, links=[16, 18]),
        Path(18, 0.059, 0.463, links=[17, 19]),
        Path(19, 0.057, 0.438, links=[18, 20]),
        Path(20, 0.057, 0.414, links=[19, 21, 86]),
        Path(21, 0.07, 0.376, links=[20, 22]),
        Path(22, 0.057, 0.336, links=[21, 23]),
        Path(23, 0.055, 0.31, links=[22, 24]),
        Path(24, 0.054, 0.279, links=[23, 25]),
        Path(25, 0.068, 0.247, links=[24, 26]),
        Path(26, 0.114, 0.221, links=[25, 27]),
        Path(27, 0.155, 0.196, links=[26, 28]),
        Path(28, 0.184, 0.188, links=[27, 29]),
        Path(29, 0.259, 0.149, links=[28, 30]),
        Path(30, 0.341, 0.172, links=[29, 31]),
        Path(31, 0.38, 0.171, links=[30, 32]),
        Path(32, 0.439, 0.187, links=[31, 33]),
        Path(33, 0.484, 0.197, links=[32, 34]),
        Path(34, 0.516, 0.2, links=[33, 35]),
        Path(35, 0.548, 0.204, links=[34, 36]),
        Path(36, 0.582, 0.214, links=[35, 37]),
        Path(37, 0.661, 0.224, links=[36, 38]),
        Path(38, 0.711, 0.278, links=[37, 39]),
        Path(39, 0.732, 0.299, links=[38, 40]),
        Path(40, 0.755, 0.325, links=[39, 41]),
        Path(41, 0.754, 0.372, links=[40, 42]),
        Path(42, 0.802, 0.382, links=[41, 43]),
        Path(43, 0.821, 0.406, links=[42, 44]),
        Path(44, 0.843, 0.429, links=[43, 45]),
        Path(45, 0.877, 0.435, links=[44, 46]),
        Path(46, 0.925, 0.45, links=[45, 47, 87]),
        Path(47, 0.927, 0.499, links=[46, 48]),
        Path(48, 0.918, 0.528, links=[47, 49]),
        Path(49, 0.905, 0.558, links=[48, 50]),
        Path(50, 0.891, 0.582, links=[49, 51]),
        Path(51, 0.868, 0.61, links=[50, 52]),
        Path(52, 0.85, 0.634, links=[51, 53]),
        Path(53, 0.821, 0.659, links=[52, 54]),
        Path(54, 0.777, 0.688, links=[53, 55]),
        Path(55, 0.771, 0.737, links=[54, 56]),
        Path(56, 0.77, 0.769, links=[55, 57]),
        Path(57, 0.809, 0.807, links=[56, 58]),
        Path(58, 0.768, 0.835, links=[57, 59]),
        Path(59, 0.732, 0.852, links=[58, 60]),
        Path(60, 0.696, 0.869, links=[59, 61]),
        Path(61, 0.659, 0.88, links=[60, 62]),
        Path(62, 0.621, 0.886, links=[61, 63]),
        Path(63, 0.588, 0.888, links=[62, 64]),
        Path(64, 0.554, 0.886, links=[1, 63]),
        Path(65, 0.354, 0.485, links=[77]),
        Path(66, 0.405, 0.82, links=[3, 67]),
        Path(67, 0.411, 0.791, links=[66, 68]),
        Path(68, 0.446, 0.758, links=[67, 69]),
        Path(69, 0.395, 0.735, links=[68, 70]),
        Path(70, 0.38, 0.71, links=[69, 71]),
        Path(71, 0.38, 0.684, links=[70, 72]),
        Path(72, 0.395, 0.656, links=[71, 73]),
        Path(73, 0.429, 0.632, links=[72, 74]),
        Path(74, 0.389, 0.608, links=[73, 75]),
        Path(75, 0.37, 0.583, links=[74, 76]),
        Path(76, 0.357, 0.553, links=[75, 77]),
        Path(77, 0.354, 0.526, links=[65, 76, 78]),
        Path(78, 0.321, 0.529, links=[77, 79]),
        Path(79, 0.28, 0.515, links=[78, 80]),
        Path(80, 0.255, 0.478, links=[79, 81]),
        Path(81, 0.218, 0.512, links=[80, 82]),
        Path(82, 0.18, 0.512, links=[81, 83]),
        Path(83, 0.146, 0.505, links=[82, 84]),
        Path(84, 0.123, 0.484, links=[83, 85]),
        Path(85, 0.121, 0.446, links=[84, 86]),
        Path(86, 0.077, 0.425, links=[20, 85]),
        Path(87, 0.945, 0.495, links=[46, 88]),
        Path(88, 0.941, 0.521, links=[87, 89]),
        Path(89, 0.941, 0.553, links=[88, 90]),
        Path(90, 0.939, 0.585, links=[89, 91]),
        Path(91, 0.938, 0.618, links=[90, 92]),
        Path(92, 0.932, 0.648, links=[91, 93]),
        Path(93, 0.92, 0.683, links=[92, 94]),
        Path(94, 0.889, 0.721, links=[93]),
    ]
)

AIRPORTS = Group(
    [
        Path(1, 0.491, 0.873, links=[2, 3, 4, 9, 11, 18]),
        Path(2, 0.654, 0.788, links=[1, 5]),
        Path(3, 0.887, 0.716, links=[1, 6]),
        Path(4, 0.807, 0.804, links=[1]),
        Path(5, 0.709, 0.533, links=[2, 6, 7]),
        Path(6, 0.921, 0.451, links=[3, 5]),
        Path(7, 0.754, 0.369, links=[5, 8, 16]),
        Path(8, 0.593, 0.423, links=[7, 9, 15]),
        Path(9, 0.58, 0.61, links=[1, 8]),
        Path(10, 0.434, 0.632, links=[13, 18]),
        Path(11, 0.188, 0.677, links=[1, 12]),
        Path(12, 0.118, 0.448, links=[11, 14]),
        Path(13, 0.25, 0.479, links=[10, 14, 15]),
        Path(14, 0.205, 0.231, links=[12, 13, 17]),
        Path(15, 0.477, 0.238, links=[8, 13, 17]),
        Path(16, 0.659, 0.222, links=[7]),
        Path(17, 0.257, 0.149, links=[14, 15]),
        Path(18, 0.443, 0.757, links=[1, 10, 13]),
    ]
)
