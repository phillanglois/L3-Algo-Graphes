from ipywidgets import Button, Dropdown, VBox, HBox, Widget  # type: ignore
from bqplot import Figure, LinearScale, Lines, Tooltip  # type: ignore
import time
from rush_hour import RushHour, Plateau, couleurs


class RushHourApplication(VBox):
    def __init__(self) -> None:
        self.niveau = Dropdown(
            options=[("Niveau {}".format(i), i) for i in RushHour.niveaux()]
        )
        self.niveau.observe(lambda widget: self.change_niveau(widget.owner.value))

        self.voiture = Dropdown(options=[])
        self.modele = Plateau(1)
        self.vue = Figure(
            scale_x=LinearScale(min=0, max=self.modele.dimension),
            scale_y=LinearScale(min=self.modele.dimension, max=0),
        )
        self.vue.layout.width = "75ex"
        self.vue.layout.width = "75ex"
        self.vue.layout.height = self.vue.layout.width

        self.vue.vue_voitures = {}
        for lettre, couleur in couleurs.items():
            vue_voiture = Lines(
                x=[],
                y=[],
                scales={"x": self.vue.scale_x, "y": self.vue.scale_y},
                fill="inside",
                colors=[couleurs[lettre]],
                visible=False,
                tooltip=Tooltip(fields=["lettre"], labels=[lettre], show_labels=True),
            )
            vue_voiture.lettre = lettre
            vue_voiture.on_element_click(
                lambda vue_voiture, _: self.choix_voiture(vue_voiture.lettre)
            )
            self.vue.vue_voitures[lettre] = vue_voiture
        self.vue.marks = list(self.vue.vue_voitures.values())

        boutton_solution = Button(description="Solution")
        boutton_solution.on_click(self.montre_solution)
        VBox.__init__(
            self,
            [
                HBox([self.niveau, boutton_solution]),
                self.vue,
                self.boutton_direction("U"),
                HBox(
                    [
                        self.boutton_direction("L"),
                        self.voiture,
                        self.boutton_direction("R"),
                    ]
                ),
                self.boutton_direction("D"),
            ],
        )
        self.layout.align_items = "center"
        self.change_niveau(1)

    # Vues
    def boutton_direction(self, direction: str) -> Button:
        boutton = Button(description=direction)
        boutton.on_click(self.on_click_direction)
        return boutton

    # Contrôleurs
    def change_niveau(self, i: int) -> None:
        self.niveau = i
        self.modele = Plateau(i)
        self.voiture.options = self.modele.voitures.keys()
        for letter, vue_voiture in self.vue.vue_voitures.items():
            vue_voiture.visible = letter in self.modele.voitures
        self.mise_a_jour_vue()

    def montre_solution(self, boutton: Button) -> None:
        self.modele = Plateau(self.niveau)
        self.mise_a_jour_vue()
        boutton.description = "Calcul en cours ..."
        solution = RushHour.solution(self.niveau)
        assert isinstance(solution, list)
        boutton.description = "Solution"
        for coup in solution:
            modele = self.modele.deplace(coup)
            assert modele is not None
            self.modele = modele
            self.mise_a_jour_vue()
            time.sleep(1)

    def on_click_direction(self, boutton: Button) -> None:
        plateau = self.modele.deplace(self.voiture.value, boutton.description)
        if plateau is not None:
            self.modele = plateau
            self.mise_a_jour_vue()

    def choix_voiture(self, lettre: str) -> None:
        self.voiture.value = lettre

    def mise_a_jour_vue(self) -> None:
        for lettre, voiture in self.modele.voitures.items():
            cases = voiture.cases()
            xmin = min(case[1] for case in cases)
            xmax = max(case[1] for case in cases) + 1
            ymin = min(case[0] for case in cases)
            ymax = max(case[0] for case in cases) + 1
            vue_voiture = self.vue.vue_voitures[lettre]
            vue_voiture.x = [xmin, xmax, xmax, xmin]
            vue_voiture.y = ([ymin, ymin, ymax, ymax],)

    def display(self) -> Widget:
        return self.widget
