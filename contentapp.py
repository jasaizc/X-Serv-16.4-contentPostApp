#!/usr/bin/python

"""
 contentApp class
 Simple web application for managing content

 Copyright Jesus M. Gonzalez-Barahona, Gregorio Robles 2009-2015
 jgb, grex @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - March 2015
"""

import webapp


class contentApp (webapp.webApp):
    """Simple web application for managing content.

    Content is stored in a dictionary, which is intialized
    with the web content."""

    # Declare and initialize content
    content = {'/': 'Root page',
               '/page': 'A page'
               }

    def parse(self, request):
        """Return the resource name (including /)"""
        
        recurso = request.split(' ', 2)[1]
        metodo = request.split(' ', 2)[0]
        if metodo == "PUT":
            cuerpo == request.split("\r\n\r\n", 1)[1]
        elif metodo == "POST":
            print "HOLA" + request.split("\r\n\r\n", 1)[1]
            cuerpo == request.split("\r\n\r\n", 1)[1]
        else:
            cuerpo = ""
        return (metodo, recurso, cuerpo)
        
        
        

    def process(self, resourceName):
        """Process the relevant elements of the request.

        Finds the HTML text corresponding to the resource name,
        ignoring requests for resources not in the dictionary.
        """
        metodo, recurso, cuerpo = resourceName
        if metodo == "GET":        
            if recurso in self.content.keys():
                httpCode = "200 OK"
                htmlBody = "<html><body>" + self.content[recurso] \
                + "<form id='formulario' method='post'><fieldset><legend>Formulario de Ejemplo</legend><label>Recurso</label> \                    <input id='campo1' name='recurso' type='text' /><label>push</label><input id='campo2' name='push' type='text' /><input id='campo3' name='enviar' type='submit'\ value='Enviar' /></fieldset></form>"+ "</body></html>"
            else:
                httpCode = "404 Not Found"
                htmlBody = "Not Found"
        elif metodo == "PUT":
            elf.content[recurso] = cuerpo
            httpCode = "200 OK"
            htmlBody = "<html><body>" + recurso + "Vale Ahora" + self.content[recurso] \
                + "</body></html>"
            
        elif metodo == "POST":
            self.content[recurso] = cuerpo
            httpCode = "200 OK"
            htmlBody = "<html><body>" + recurso + "Vale Ahora" + self.content[recurso] \
                    + "</body></html>"
            
        elif metodo == "DELETE":   
            self.content[recurso] = cuerpo
            httpCode = "200 OK"
            htmlBody = "<html><body>" + recurso + "Vale Ahora" + self.content[recurso] \
                    + "</body></html>"
                
        return (httpCode, htmlBody)


if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1234)
