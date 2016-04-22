#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import sys


class calcRest(webapp.webApp):
    resultado = str(0);
    def parse(self, request):
        try:
            metodo = request.split()[0]
            recurso = request.split()[1]
            if metodo != 'GET':
                cuerpo = request.split('\r\n\r\n')[1]
            else:
                cuerpo = ""
        except IndexError:
            return None

        return (metodo, recurso, cuerpo)

    def process(self, parsedRequest):
        try:
            metodo, recurso, cuerpo = parsedRequest
        except TypeError:
            httpCode = '400 Bad Request'
            htmlResp = '<html><body>Solicitud errónea </body></html>'
            return (httpCode, htmlResp)metodo, recurso, cuerpo = parsedRequest

        if metodo == 'PUT':
            httpCode = '200 OK'
            numero1 = cuerpo.split()[0]
            operacion = cuerpo.split()[1]
            numero2 = cuerpo.split()[2]

            if operacion == '-':
                self.resultado = str(int(numero1) - int(numero2))
                htmlResp = '<html><body>' + numero1 + ' - ' + numero2 + \
                            ' = ' + self.resultado + '</body></html>'
            elif operacion == '+':
                self.resultado = str(int(numero1) + int(numero2))
                htmlResp = '<html><body>' + numero1 + '  +' + numero2 + \
                            ' = ' + self.resultado + '</body></html>'
            elif operacion == '*':
                self.resultado = str(int(numero1) * int(numero2))
                htmlResp = '<html><body>' + numero1 + ' * ' + numero2 + \
                            ' = ' + self.resultado + '</body></html>'
            elif operacion == '/':
                try:
                    self.resultado = str(int(numero1) / int(numero2))
                except ZeroDivisionError:
                    httpCode = '400 Bad request'
                    htmlResp = "No puedes dividir entre cero"
                    return (httpCode, htmlResp)
                htmlResp = '<html><body>' + numero1 + ' / ' + numero2 + \
                            ' = ' + self.resultado + '</body></html>'
            else:
                httpCode = '400 Bad request'
                htmlResp = 'Operacion no aceptada'
        elif metodo == 'GET':
            httpCode = "200 OK"
            htmlResp = '<html><body>' + 'Solucion: '\
                        + self.resultado + '</body></html>'
        else:
            httpCode = '405 Method not Allowed'
            htmlResp = '<html><body>Metodo no permitido</body></html>'
        return (httpCode, htmlResp)
if __name__ == "__main__":
    try:
        testCalculadoraRESTApp = calcRest("localhost", 1234)
    except KeyboardInterrupt:
        print "Closing binded socket"
        mySocket.close()
