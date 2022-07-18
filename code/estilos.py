layers = iface.mapCanvas().layers()
path =  'C:/Users/lpzam/OneDrive/Área de Trabalho/Carregar estilos/estilos/'

def define_styles(style):
	layer.loadNamedStyle(path + style)
	renderer = layer.renderer()
	myRenderer = renderer.clone()
	layer.setRenderer(myRenderer)
	layer.triggerRepaint()

for layer in layers:

	if layer.name() == 'Pasto':
		define_styles('Pasto.qml')

	elif layer.name() == 'Floresta':
		define_styles('Floresta.qml')

	elif layer.name() == 'Orientacao':
		define_styles('Orientacao.qml')

	elif layer.name() == 'Aeroportos':
		define_styles('Aeroportos.qml')