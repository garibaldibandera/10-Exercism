import re


class PhoneNumber:
    def __init__(self, number):
        numeroTel = "".join([x for x in number if x.isdigit()])
        if(numeroTel.startswith('1')):
            numeroTel = numeroTel[1:]
        if(not re.match('^[2-9][0-9]{2}[2-9][0-9]{6}$', numeroTel)):
            raise ValueError('Formato no valido')
        self.number ,self.codigoArea = numeroTel,numeroTel[:3]

    def pretty(self):
        return "({}) {}-{}".format(self.codigoArea, self.number[3:6], self.number[6:])
    
