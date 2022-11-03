import re

class IPv4NetworkCalculator():
    def __init__(self, ip='', prefixo='', mask='', rede='', broadcast='', num_ips=''):
        self.ip = ip
        self.prefixo = prefixo
        self.mask = mask
        self.rede = rede
        self.broadcast = broadcast
        self.num_ips = num_ips

        if self.ip == '':
            raise ValueError("IP não enviado")

        self.ip_tem_prefixo()
        
        if not self.is_ip():
            raise ValueError("IP Inválido")

        if not self.prefixo and not self.mask:
            raise ValueError("Pelo menos o Prefixo ou a Máscara devem ser enviados")

        if self.mask :
            self.mask_bin = self.ip_decimal_for_binary(ip=self.mask)
            self.prefixo_mascara()

        self.set_num_ips()
        self.set_rede_broadcast()
        self.mask_prefixo()

    def set_rede_broadcast(self):
        ip_bin = self.ip_decimal_for_binary(self.ip)
        ip_bin = ip_bin.replace('.', '')
        
        rede = ''
        broadcast = ''
        for cont, bit in enumerate(ip_bin):
            if cont < int(self.prefixo):
                rede += str(bit)
                broadcast += str(bit)
            else:
                rede += '0'
                broadcast += '1'
        self.rede = self.ip_binary_for_dec(rede)
        self.broadcast = self.ip_binary_for_dec(broadcast)
    
    def mask_prefixo(self):
        mask_bin = ''
        for i in range(32):
            if i < int(self.prefixo):
                mask_bin += '1'
            else:
                mask_bin += '0'
        
        mask_dec = self.ip_binary_for_dec(mask_bin)
        self.mask = mask_dec



    def ip_binary_for_dec(self, ip=''):
        new_ip = str(int(ip[0:8], 2)) + '.'
        new_ip += str(int(ip[8:16], 2)) + '.'
        new_ip += str(int(ip[16:24], 2)) + '.'
        new_ip += str(int(ip[24:32], 2)) 

        return new_ip

    def set_num_ips(self):
        host_bits = 32-int(self.prefixo)
        self.num_ips = pow(2, host_bits)


    def prefixo_mascara(self):
        mask_bin = self.mask_bin.replace('.', '')
        cont = 0

        for bit in mask_bin:
            if bit == '1':
                cont +=1
        self.prefixo = cont

    
    def ip_decimal_for_binary(self, ip=''):
        if not ip:
            ip = self.ip
        
        bloco_ip = ip.split('.')
        ip_bin = list()

        for bloco in bloco_ip:
            binario = bin(int(bloco))
            binario = binario [2:].zfill(8)
            ip_bin.append(binario)

        ip_bin = '.'.join(ip_bin)
        
        return ip_bin
    
    
    def is_ip(self):
        ip_regexp = re.compile('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$')

        if ip_regexp.search(self.ip):
            return True
        
        return False


    def ip_tem_prefixo(self):
        ip_prefixo_regexp = re.compile('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/[0-9]{1,3}$')

        if not ip_prefixo_regexp.search(self.ip):
            return

        divide_ip = self.ip.split('/')
        self.ip = divide_ip [0]
        self.prefixo = divide_ip [1]

    def get_all(self):
        return {
            'IP':self.ip,
            'Prefixo':self.prefixo,
            'Máscara':self.mask,
            'Rede':self.rede,
            'Broadcast':self.broadcast, 
            'Número de IPs em cada Rede':self.num_ips,
        }







if __name__ == '__main__':
    ipv4 = IPv4NetworkCalculator(ip=input('Digite seu número IP [Prefixo Necessário]: '))
    print( ipv4.get_all() )