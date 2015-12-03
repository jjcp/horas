import json
import os
from datetime import datetime


class Horas(object):

    def __init__(self, ruta_hs='~/.horas.json'):
        self.ruta_hs = os.path.expanduser(ruta_hs)
        self.formato_datetime = '%Y-%m-%d %H:%M:%S'

    def inicio(self, nombre):
        hs = self._leer_hs()
        self._cerrar_registros(hs)
        nombre = nombre or 'horas-sueltas'
        hs.setdefault(nombre, []).append({
            'inicio': datetime.utcnow().strftime(self.formato_datetime)
        })
        self._salvar_hs(hs)

    def fin(self):
        hs = self._leer_hs()
        self._cerrar_registros(hs)
        self._salvar_hs(hs)

    def _leer_hs(self):
        return json.load(open(self.ruta_hs, 'r'))

    def _salvar_hs(self, hs):
        with open(self.ruta_hs, 'w') as f:
            f.write(json.dumps(hs, indent=4))
            f.write('\n')

    def _cerrar_registros(self, hs):
        for tarea in hs.values():
            for registro in tarea:
                if 'fin' not in registro:
                    registro['fin'] = datetime.utcnow() \
                                              .strftime(self.formato_datetime)
