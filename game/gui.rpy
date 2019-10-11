################################################################################
## Initialisation
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Appelé gui.init réinitialise les styles à leurs valeurs par défaut et
## initialise la largeur et la hauteur du jeu.
init python:
    gui.init(800, 600)



################################################################################
## GUI Configuration Variables
################################################################################


## Couleurs ####################################################################
##
## Les couleurs du texte dans l’interface.

## Une couleur utilisée dans l’interface pour mettre l’accent sur un texte
## (surbrillance).
define gui.accent_color = '#0099cc'

## La couleur utilisée pour le texte d’un bouton quand il n’a jamais été
## sélectionné ou survolé.
define gui.idle_color = '#888888'

## La petite couleur est utilisé pour les textes courts qui nécessitent d’être
## assombris ou éclairés pour obtenir le même effet.
define gui.idle_small_color = '#aaaaaa'

## Cette couleur est utilisée pour les boutons et les barres qui sont survolées.
define gui.hover_color = '#66c1e0'

## Cette couleur est utilisé pour le texte d’un bouton sélectionné, mais qui n’a
## pas le focus. Un bouton est sélectionné s’il est sur l’écran actuel ou si
## c’est la valeur de préférence.
define gui.selected_color = '#ffffff'

## La couleur utilisée pour le texte d’un bouton qui ne peut pas être
## sélectionné.
define gui.insensitive_color = '#8888887f'

## Couleurs utilisées pour les portions de barres qui ne sont pas remplies.
## Elles ne sont pas utilisées directement, mais quand les fichiers d’images
## sont régénérés.
define gui.muted_color = '#003d51'
define gui.hover_muted_color = '#005b7a'

## Les couleurs utilisées pour les dialogues et les menus de choix.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Polices et tailles de police ################################################

## Les polices utilisées pour le texte du jeu.
define gui.text_font = "DejaVuSans.ttf"

## Les polices utilisées pour le nom des personnages.
define gui.name_text_font = "DejaVuSans.ttf"

## Les polices utilisées pour les textes « hors du jeu ».
define gui.interface_text_font = "DejaVuSans.ttf"

## La taille normale pour les dialogues.
define gui.text_size = 14

## La taille pour le nom des personnages.
define gui.name_text_size = 19

## La taille du texte dans l’interface de jeu.
define gui.interface_text_size = 14

## La taille des libellés dans l’interface de jeu.
define gui.label_text_size = 15

## La taille du texte dans la zone de notification.
define gui.notify_text_size = 10

## La taille du titre du jeu.
define gui.title_text_size = 32


## Menu du jeu et menu principal ###############################################

## Les images utilisées pour le menu principal et le menu du jeu.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Dialogue ####################################################################
##
## Ces variables contrôlent comment les dialogues sont affichés une ligne à la
## fois.

## La hauteur de la fenêtre contenant les dialogues.
define gui.textbox_height = 116

## L’emplacement vertical de la zone de texte à l’écran. 0.0 pour le haut, 0.5
## pour le centre et 1.0 pour le bas.
define gui.textbox_yalign = 1.0


## L’emplacement relatif à la zone de texte du nom du personnage en train de
## parler. La valeur peut être un nombre entier de pixels depuis la gauche ou le
## haut ou 0.5 pour le centre.
define gui.name_xpos = 150
define gui.name_ypos = 0

## L’alignement horizontal du nom du personnage. La valeur peut être 0.0 pour un
## alignement à gauche, 0.5 pour le centrer et 1.0 pour un alignement à droite.
define gui.name_xalign = 0.0

## La largeur, profondeur et les bords de la zone contenant le nom du personnage
## ou « None » pour le dimensionner automatiquement.
define gui.namebox_width = None
define gui.namebox_height = None

## Les bordures de la zone contenant le nom du personnage dans l’ordre suivant
## gauche, haut, droite, bas.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Si « True » (vrai), l’arrière plan de zone du nom sera en mosaïque, si
## « False »(faux), l’arrière plan de la zone du nom sera mis à l’échelle.
define gui.namebox_tile = False


## L’emplacement du dialogue relatif à la zone de texte. La valeur peut être un
## nombre entier de pixels depuis la gauche ou le haut ou 0.5 pour le centre.
define gui.dialogue_xpos = 168
define gui.dialogue_ypos = 32

## La largeur maximale en pixels de la zone de dialogue.
define gui.dialogue_width = 465

## L’alignement horizontal de la zone de dialogue. La valeur peut être 0.0 pour
## un alignement à gauche, 0.5 pour le centrer et 1.0 pour un alignement à
## droite.
define gui.dialogue_text_xalign = 0.0


## Boutons #####################################################################
##
## Ces variables, ainsi que les fichiers d’image dans gui/button, contrôlent la
## façon d’afficher les boutons et leur aspect.

## La largeur et la hauteur d’un bouton en pixels. Si aucune valeur n’est
## renseignée (None), Ren’Py calcule la taille.
define gui.button_width = None
define gui.button_height = None

## Les bordures de chaque côté du bouton dans l’ordre suivant gauche, haut,
## droit, bas.
define gui.button_borders = Borders(3, 3, 3, 3)

## Si « True » (vrai), l’image d’arrière plan sera en mosaïque, si
## « False »(faux), elle sera mise à l’échelle.
define gui.button_tile = False

## La police utilisée par le bouton.
define gui.button_text_font = gui.interface_text_font

## La taille du texte utilisée pour le bouton.
define gui.button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.button_text_xalign = 0.0


## Ces variables surchargent les paramètres par défaut pour différents types de
## boutons. Veuillez consulter la documentation de l’interface de jeu (GUI) pour
## les types de boutons disponibles et leurs usages.
##
## Ces personnalisations sont utilisées par l’interface par défaut :

define gui.radio_button_borders = Borders(12, 3, 3, 3)

define gui.check_button_borders = Borders(12, 3, 3, 3)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(7, 3, 7, 3)

define gui.quick_button_borders = Borders(7, 3, 7, 0)
define gui.quick_button_text_size = 9
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Vous pouvez également ajouter vos propres personnalisations en ajoutant des
## variables correctement nommées. Par exemple, vous pouvez décommanter la ligne
## suivante pour personnaliser la largeur du bouton de navigation.

# define gui.navigation_button_width = 250


## Boutons pour les choix ######################################################
##
## Les boutons pour les choix (Choice buttons) sont utilisés dans le jeu pour
## permettre au joueur de choisir telle ou telle action, tel ou tel dialogue.

define gui.choice_button_width = 494
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(63, 4, 63, 4)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"


## Boutons des emplacements de fichiers. #######################################
##
## Un bouton d’emplacement de fichier est un type spécial de bouton. Il contient
## une vignette et un texte décrivant le contenu de la sauvegarde présente dans
## l’emplacement. Un emplacement de sauvegarde utilise une image dans gui/
## button, comme les autres types de bouton.

## Le bouton d’emplacement de sauvegarde.
define gui.slot_button_width = 173
define gui.slot_button_height = 129
define gui.slot_button_borders = Borders(7, 7, 7, 7)
define gui.slot_button_text_size = 9
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## La largeur et la hauteur des vignettes de sauvegarde utilisée pour les
## emplacements de sauvegarde.
define config.thumbnail_width = 160
define config.thumbnail_height = 90

## Le nombre de colonnes et de lignes pour la grille des emplacements de
## sauvegarde.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Positionnement et espacement ################################################
##
## Ces variables contrôlent l’espacement et le positionnement des différents
## éléments de l’interface utilisateur.

## La position sur le côté gauche des boutons de navigation, relatif au côté
## gauche de l'écran.
define gui.navigation_xpos = 25

## La position vertical du l’indicateur de saut des dialogues.
define gui.skip_ypos = 7

## La position verticale de la zone de notification.
define gui.notify_ypos = 29

## L’espacement entre les différents choix du menu.
define gui.choice_spacing = 14

## Boutons dans la section de navigation du menu principal et du menu de jeu.
define gui.navigation_spacing = 3

## Contrôle l’espacement entre les préférences.
define gui.pref_spacing = 7

## Contrôle l’espacements entre les boutons de préférences.
define gui.pref_button_spacing = 0

## L’espacement entre les boutons de page.
define gui.page_spacing = 0

## L’espacement entre les emplacements de sauvegarde.
define gui.slot_spacing = 7

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


## Cadres ######################################################################
##
## Ces variables contrôlent le look des cadres qui peuvent contenir les
## composants de l’interface utilisateur quand un overlay ou une fenêtre ne sont
## pas présents.

## Generic frames.
define gui.frame_borders = Borders(3, 3, 3, 3)

## Le cadre qui est utilisé par les écrans de confirmation.
define gui.confirm_frame_borders = Borders(25, 25, 25, 25)

## Le cadre qui est utilisé par l’écran de saut des dialogues.
define gui.skip_frame_borders = Borders(10, 4, 32, 4)

## Le cadre qui est utilisé par la zone de notification.
define gui.notify_frame_borders = Borders(10, 4, 25, 4)

## Est-ce que les arrière-plans des cadres doivent être en mosaïque ?
define gui.frame_tile = False


## Barres, ascenseurs et curseurs ##############################################
##
## Ceux-ci contrôlent le look et la taille des barres, des ascenseurs et des
## curseurs.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## La hauteur des barres, des ascenseurs et des curseurs horizontaux. La largeur
## des barres, des ascenseurs et des curseurs verticaux.
define gui.bar_size = 16
define gui.scrollbar_size = 8
define gui.slider_size = 16

## « True » (Vrai)  si les images de barres doivent être en mosaïques.
## « False »(Faux) si elles doivent être mise à l'échelle (étirement).
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Bordures horizontales.
define gui.bar_borders = Borders(3, 3, 3, 3)
define gui.scrollbar_borders = Borders(3, 3, 3, 3)
define gui.slider_borders = Borders(3, 3, 3, 3)

## Bordures verticales.
define gui.vbar_borders = Borders(3, 3, 3, 3)
define gui.vscrollbar_borders = Borders(3, 3, 3, 3)
define gui.vslider_borders = Borders(3, 3, 3, 3)

## Que faire avec les ascenseurs non utilisables dans le GUI ? « hide » les
## cache tandis que « None » les affiche.
define gui.unscrollable = "hide"


## Historique ##################################################################
##
## L’écran de l’historique affiche les dialogues que le joueur vient de lire.

## Le nombre de blocs que l’historique de dialogue Ren’Py va conserver.
define config.history_length = 250

## La hauteur de l’écran historique ou « None » pour calculer la hauteur au prix
## d’une légère perte de performance.
define gui.history_height = 88

## La position, largeur et alignement du label donnant le nom du personnage en
## train de parler.
define gui.history_name_xpos = 97
define gui.history_name_ypos = 0
define gui.history_name_width = 97
define gui.history_name_xalign = 1.0

## La position, largeur et alignement de la zone de dialogue.
define gui.history_text_xpos = 107
define gui.history_text_ypos = 2
define gui.history_text_width = 463
define gui.history_text_xalign = 0.0


## Mode NVL ####################################################################
##
## L’écran du mode NVL affiche les dialogues prononcés par les personnages eux-
## mêmes en mode NVL.

## Les bordures de l’arrière-plan de la fenêtre en mode NVL.
define gui.nvl_borders = Borders(0, 7, 0, 13)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## La hauteur d’une entrée en mode NVL. Initialisez-la à « None » pour que la
## hauteur des entrées s’ajuste automatiquement.
define gui.nvl_height = 72

## L’espacement entre les entrées en mode NVL quand gui.nvl_height est à
## « None » et entre les entrées en mode NVL et le menu en mode NVL.
define gui.nvl_spacing = 7

## La position, largeur et alignement du label donnant le nom du personnage en
## train de parler.
define gui.nvl_name_xpos = 269
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 94
define gui.nvl_name_xalign = 1.0

## La position, largeur et alignement de la zone de dialogue.
define gui.nvl_text_xpos = 282
define gui.nvl_text_ypos = 5
define gui.nvl_text_width = 369
define gui.nvl_text_xalign = 0.0

## La position, profondeur et l’alignement du text nvl_tought (Le texte prononcé
## par le personnage nvl_narrator).
define gui.nvl_thought_xpos = 150
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 488
define gui.nvl_thought_xalign = 0.0

## La position de nvl menu_buttons.
define gui.nvl_button_xpos = 282
define gui.nvl_button_xalign = 0.0

## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Mobile devices
################################################################################

init python:

    ## Ceci augmente la taille des boutons d’accès rapide pour les rendre plus
    ## accessibles sur les tablettes et les téléphones.
    if renpy.variant("touch"):

        gui.quick_button_borders = Borders(25, 9, 25, 0)

    ## Ceci change la taille et l’espacement de différents élements de la GUI
    ## pour s’assurer qu’ils soient visibles sur les téléphones.
    if renpy.variant("small"):

        ## Tailles des polices.
        gui.text_size = 19
        gui.name_text_size = 23
        gui.notify_text_size = 16
        gui.interface_text_size = 19
        gui.button_text_size = 19
        gui.label_text_size = 22

        ## Ajuste la position de la zone de texte.
        gui.textbox_height = 150
        gui.name_xpos = 50
        gui.text_xpos = 57
        gui.text_width = 688

        ## Change the size and spacing of various things.
        gui.slider_size = 23

        gui.choice_button_width = 775

        gui.navigation_spacing = 13
        gui.pref_button_spacing = 7

        gui.history_height = 119
        gui.history_text_width = 432

        gui.quick_button_text_size = 13

        ## Remplit le canvas du bouton.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Mode NVL.
        gui.nvl_height = 107

        gui.nvl_name_width = 191
        gui.nvl_name_xpos = 204

        gui.nvl_text_width = 572
        gui.nvl_text_xpos = 216
        gui.nvl_text_ypos = 4

        gui.nvl_thought_width = 775
        gui.nvl_thought_xpos = 13

        gui.nvl_button_width = 775
        gui.nvl_button_xpos = 13



