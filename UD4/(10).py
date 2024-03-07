class Tablet:

    def __init__(self):
        # self.creador = creador
        # self.tamano_pantalla = tamano_pantalla
        # self.num_cores = num_cores
        self.apps = []
        self.status = False

    def power_on(self):
        self.status = True

    def power_off(self):
        self.status = False

    def install_app(self, app):

        if app not in self.apps:
            self.apps.append(app)
            return(f"La app {app} ha sido instalada correctamente.")

        else:
            return(f"La app {app} ya esta instalada no se puede volver a instalar.")

    def uninstall_app(self, app):

        if app in self.apps:
            self.apps.remove(app)
            print(f"La app {app} ha sido desinstalada correctamente.")

        else:
            return(f"La app {app} no esta instalada, no se puede desinstalar.")

Tablet_de_Pep = Tablet()

Tablet_de_Pep.power_on()

print(Tablet_de_Pep.install_app("Spotify"))
print(Tablet_de_Pep.install_app("Xampp"))
print(Tablet_de_Pep.uninstall_app("Spotify"))
print(Tablet_de_Pep.uninstall_app("Google Chrome"))

Tablet_de_Pep.power_off()