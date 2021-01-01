from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import string

class MainWindow(Screen):
    pass

class Encryption(Screen):
    plaintext = ObjectProperty(None)
    key_e = ObjectProperty(None)
    # use specific key to encrypt text message
    def Encrypt(self):
        k = str(self.key_e.text).lower()
        p = str(self.plaintext.text).lower()
        list_plaintext = [char for char in p]
        list_key = [char for char in k]
        alpha_l = list(string.ascii_lowercase)
        encrypted_text = []
        #list_key = self.key1_e()
        #list_key = self.key2_e()
        list_key = self.key3_e()
        for x,y in zip(list_plaintext,list_key):
            m = (alpha_l.index(x)+(alpha_l.index(y)))%26
            encrypted_text.append(alpha_l[m])
        encrypted_text = ''.join(encrypted_text)
        new_key = ''.join(list_key)
        pop = Popup(title="Result", content=Label(text=str("Ciphertext: "+encrypted_text + " New key: "+new_key)), size_hint=(None, None),
                    size=(400, 400))
        pop.open()
# create specific key to improve security
    def key1_e(self):
        p = str(self.plaintext.text).lower()
        k = str(self.key_e.text).lower()
        list_plaintext = [char for char in p]
        list_key = [char for char in k]
        if len(list_key) < len(list_plaintext):
            i = 0
            while len(list_key) != len(list_plaintext):
                list_key.append(list_key[i])
                i += 1
        return list_key

# create specific key to improve security

    def key2_e(self):
        p = str(self.plaintext.text).lower()
        k = str(self.key_e.text).lower()
        list_plaintext = [char for char in p]
        list_key = [char for char in k]
        if len(list_key) < len(list_plaintext):
            i = 0
            while len(list_key) != len(list_plaintext):
                list_key.append(list_plaintext[i])
                i += 1
        return list_key

    # create specific key to improve security
    def key3_e(self):
        p = str(self.plaintext.text).lower()
        k = str(self.key_e.text).lower()
        list_plaintext = [char for char in p]
        list_key = [char for char in k]
        current_l = list_plaintext
        if len(list_key) < len(list_plaintext):
            i = 0
            while len(list_key) != len(list_plaintext):
                scramble_key = list_plaintext
                scramble_key.sort(reverse=True)
                list_key.append(current_l[i])
                i += 1
            list_key = scramble_key
        return list_key

#decrpt specific text using a specific key
class Decryption (Screen):
    ciphertext = ObjectProperty(None)
    key_d = ObjectProperty(None)
    def Decrypt(self):
        c = str(self.ciphertext.text).lower()
        k = str(self.key_d.text).lower()
        list_encrypted_text = [char for char in c]
        alpha = list(string.ascii_lowercase)
        list_key = [char for char in k]
        message = []
        if len(list_key) < len(list_encrypted_text):
            i = 0
            while len(list_key) != len(list_encrypted_text):
                list_key.append(list_key[i])
                i += 1
        for x, y in zip(list_encrypted_text, list_key):
            m = (alpha.index(x) - (alpha.index(y))) % 26
            message.append(alpha[m])
        message = ''.join(message)
        pop = Popup(title="Result",
                    content=Label(text="plain text: "+message),
                    size_hint=(None, None),
                    size=(400, 400))
        pop.open()



# kivy window manager allow easy access between different window
class WindowManager(ScreenManager):
    pass

    def authentication(self):
        pass



kv = Builder.load_file("vigenere.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()