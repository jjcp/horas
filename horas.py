import json
import os
import sys
from datetime import datetime, timedelta


class Horas(object):

    def __init__(self, ruta_hs='~/.horas.json'):
        self.ruta_hs = os.path.expanduser(ruta_hs)
        self.formato_datetime = '%Y-%m-%d %H:%M:%S'
        self.formato_fecha = '%Y-%m-%d'

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

    def reporte(self):
        hs = self._leer_hs()

        reporte = {}
        tarea_activa = {}
        for nombre, tarea in hs.items():
            for registro in tarea:
                inicio = datetime.strptime(registro['inicio'],
                                           self.formato_datetime)

                fecha = inicio.strftime(self.formato_fecha)

                if 'fin' in registro:
                    reporte.setdefault(fecha, {})
                    fin = datetime.strptime(registro['fin'],
                                            self.formato_datetime)
                    delta = reporte[fecha].setdefault(nombre, timedelta())
                    reporte[fecha][nombre] += delta + (fin - inicio)
                else:
                    tarea_activa.setdefault(fecha, {})
                    fin = datetime.utcnow().replace(microsecond=0)
                    delta = tarea_activa[fecha].setdefault(nombre, timedelta())
                    tarea_activa[fecha][nombre] = fin - inicio

        for fecha, datos in tarea_activa.items():
            sys.stdout.write('%s ----- Activa -----\n' % fecha)
            for tarea, delta in datos.items():
                sys.stdout.write('    %s : %s\n' % (delta, tarea))

        for fecha, datos in reporte.items():
            sys.stdout.write('%s ------------------\n' % fecha)
            for tarea, delta in datos.items():
                sys.stdout.write('    %s : %s\n' % (delta, tarea))

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
