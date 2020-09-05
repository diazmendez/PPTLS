from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from random import randint
from kivy.properties import ObjectProperty, StringProperty

lista=("piedra","papel","tijera","lagarto","spock")

Sentencias={
    "piti": "La piedra rompe la tijera.",
    "pila": "La piedra aplasta al lagarto.",
    "papi": "El papel envuelve la piedra.",
    "pasp": "El papel refuta a spock.",
    "tipa": "La tijera corta el papel.",
    "tila": "La tijera decapita al lagarto.",
    "lapa": "El lagarto se come el papel.",
    "lasp": "El lagarto envenena a spock.",
    "sppi": "Spock vaporiza la piedra.",
    "spti": "Spock destroza la tijera."
}

JudgingTree={
    "piedra": {
        "papel": (-1,"papi"),
        "tijera": (1, "piti"),
        "lagarto": (1, "pila"),
        "spock": (-1, "sppi")
    },
    "papel": {
        "piedra": (1, "papi"),
        "tijera": (-1, "tipa"),
        "lagarto": (-1, "lapa"),
        "spock": (1, "pasp")
    },
    "tijera": {
        "piedra": (-1, "piti"),
        "papel": (1, "tipa"),
        "lagarto": (1, "tila"),
        "spock": (-1, "spti")
    },
    "lagarto": {
        "piedra": (-1, "pila"),
        "papel": (1, "lapa"),
        "tijera": (-1, "tila"),
        "spock": (1, "lasp")
    },
    "spock": {
        "piedra": (1, "sppi"),
        "papel": (-1, "pasp"),
        "tijera": (1, "spti"),
        "lagartp": (-1, "lasp")
    }
}



kv = Builder.load_file("PPTLS.kv")




class MyGrid(Widget):

    wd_bottom = ObjectProperty(None)
    wd_up = ObjectProperty(None)

    wd_piedra = ObjectProperty(None)
    wd_papel = ObjectProperty(None)
    wd_tijera = ObjectProperty(None)
    wd_lagarto = ObjectProperty(None)
    wd_spock = ObjectProperty(None)

    selection = lista[randint(0, 4)]

    def btn(self, instance):

        wd_bottom = self.wd_bottom
        wd_up = self.wd_up

        wd_piedra = self.wd_piedra
        wd_papel = self.wd_papel
        wd_tijera = self.wd_tijera
        wd_lagarto = self.wd_lagarto
        wd_spock = self.wd_spock


        wd_piedra.disabled_color = 0,0,0,.4
        wd_papel.disabled_color = 0,0,0,.4
        wd_tijera.disabled_color = 0,0,0,.4
        wd_lagarto.disabled_color = 0,0,0,.4
        wd_spock.disabled_color = 0,0,0,.4

        wd_piedra.disabled = True
        if instance == "piedra":
            wd_piedra.disabled_color = 1,1,1,1
        wd_papel.disabled = True
        if instance == "papel":
            wd_papel.disabled_color = 1,1,1,1
        wd_tijera.disabled = True
        if instance == "tijera":
            wd_tijera.disabled_color = 1,1,1,1
        wd_lagarto.disabled = True
        if instance == "lagarto":
            wd_lagarto.disabled_color = 1,1,1,1
        wd_spock.disabled = True
        if instance == "spock":
            wd_spock.disabled_color = 1,1,1,1

        wd_bottom.disabled = False


        temptext = "El algoritmo escogió:\n\n\n\n\n  " + self.selection.capitalize()
        wd_up.text = temptext


        if instance == self.selection:
            print(instance + "  " + self.selection + " Iguales!")

            wd_bottom = self.wd_bottom
            wd_bottom.text = "Iguales! \n\n\n\n\n\n (click para jugar de nuevo)"
            wd_bottom.color = 0,.75,0,1

            #current_wd_bottom.text = "Iguales!"
        else:
            print(instance + '  ' + self.selection + ' ' + Sentencias[JudgingTree[instance][self.selection][1]])

            #print (JudgingTree[instance][self.selection][0])

            if JudgingTree[instance][self.selection][0] == 1:
                wd_bottom.color = 0,.75,.75,1
                juicio = "Ganaste!!!  Felicidades!... \n\n" + Sentencias[JudgingTree[instance][self.selection][1]] + "\n\n\n (click para jugar de nuevo)"
            else:
                wd_bottom.color = .5, 0, 0, 1
                juicio = "Oops!  ...nadie es perfecto. \n\n" + Sentencias[JudgingTree[instance][self.selection][1]] \
                         + "\n\n\n (click para jugar de nuevo)"

            wd_bottom.text = juicio


        pass


    def restart(self):

        self.selection = lista[randint(0, 4)]

        wd_bottom = self.wd_bottom
        wd_up = self.wd_up
        wd_piedra = self.wd_piedra
        wd_papel = self.wd_papel
        wd_tijera = self.wd_tijera
        wd_lagarto = self.wd_lagarto
        wd_spock = self.wd_spock

        wd_piedra.disabled = False
        wd_papel.disabled = False
        wd_tijera.disabled = False
        wd_lagarto.disabled = False
        wd_spock.disabled = False

        wd_bottom.disabled = True


        temptext = "El algoritmo ya ha escogido..."
        wd_up.text = temptext

        temptext = "Es tu turno!"
        wd_bottom.text = temptext
        wd_bottom.color = 1,1,1,1


    pass



class PPTLSApp(App):
    def build(self):
        return MyGrid()




if __name__ == '__main__':
    PPTLSApp().run()


