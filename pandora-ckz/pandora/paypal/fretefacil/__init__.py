#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib2 import Request,urlopen
from xml.dom import minidom as dom

def create_deliverable(sender,receiver,width,height,length,weight):
	if int(height) < 2: return 'Altura abaixo do mínimo (2cm).'
	if int(width) < 11: return 'Largura abaixo do mínimo (11cm).'
	if int(length) < 16: return 'Profundidade abaixo do mínimo (16cm).'
	deliverable = {
		'sender': sender,
		'receiver': receiver,
		'width': str(width),
		'height': str(height),
		'length': str(length),
		'weight': str(weight),
	}	
	return deliverable

def build_request(d):
	url = 'https://ff.paypal-brasil.com.br/FretesPayPalWS/WSFretesPayPal'
	headers = {
		'Content-Type': 'text/xml; charset=utf-8',
		'SoapAction': '%s/getPreco' % url
	}
	xml = """<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:shipping=\"https://ff.paypal-brasil.com.br/FretesPayPalWS\">
        <soapenv:Header />
          <soapenv:Body>
            <shipping:getPreco>
              <cepOrigem>%s</cepOrigem>
              <cepDestino>%s</cepDestino>
              <largura>%s</largura>
              <altura>%s</altura>
              <profundidade>%s</profundidade>
              <peso>%s</peso>
            </shipping:getPreco>
          </soapenv:Body>
        </soapenv:Envelope>""" % (d['sender'],d['receiver'],d['width'],d['height'],d['length'],d['weight'])
	return url,headers,xml

def delivery_value(deliverable,tornado=False):
	url,headers,xml = build_request(deliverable)
	if tornado:
		import tornadoweb
		value = tornadoweb.request(url,headers,xml)
	else:
		req = Request(url,xml,headers)
		value = urlopen(req).read()
	val = dom.parseString(value).getElementsByTagName('return')[0].childNodes[0].wholeText
	if '-2.0' in val: return 'Não foi possível calcular o frete.'
	else: return '%.2f' % float(val)
