layers = iface.mapCanvas().layers()
path =  'C:/Users/lpzam/OneDrive/Área de Trabalho/Carregar estilos/estilos/'

def define_styles(style):
	layer.loadNamedStyle(path + style)
	renderer = layer.renderer()
	myRenderer = renderer.clone()
	layer.setRenderer(myRenderer)
	layer.triggerRepaint()

for layer in layers:
	print(layer.name())
	if layer.name() == 'Contornos':
		define_styles('Contornos.qml')

	elif layer.name() == 'Talhoes':
		define_styles('Perimetro.qml')

	elif layer.name() == 'Slope':
		define_styles('Slope.qml')

	elif layer.name() == 'MDT':
		define_styles('Altimetria.qml')

	elif layer.name() == 'Channel Network':
		define_styles('Fluxos.qml')

	elif layer.name() == 'Terracos':
		define_styles('Terracos.qml')

	elif layer.name() == 'Carreadores':
		define_styles('Carreadores.qml')

	elif layer.name() == 'Plantio':
		define_styles('Plantio.qml')