vermelho = 'B4'
infra = 'B5'

def ndvi(imagem):
    ndvi = imagem.expression('(infra - vermelho) / (infra + vermelho)', {'infra': imagem.select(nir), 'vermelho': imagem.select(red)}).rename('ndvi')
    return imagem.addBands(ndvi)

colecao.map(ndvi)
#extrair a imagem mediana da coleção:
imagem = colecao.median()
#Pegar a imagem em rgb
print(imagem.select(['B4','B3','B2']).getDownloadUrl())
