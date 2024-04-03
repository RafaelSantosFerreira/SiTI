Para formatar o texto anterior para um arquivo README.md do Git, você pode seguir a estrutura de Markdown a seguir para organizar o conteúdo de forma clara e atraente:

```markdown
# Cálculo de SI e TI para PNGs

Este documento detalha o processo de cálculo dos índices de Similaridade Estrutural (SI) e de Intensidade Temporal (TI) para imagens PNG geradas a partir de arquivos de vídeo, utilizando uma linha de comando específica com o ffmpeg.

## Gerando PNGs com ffmpeg

Para gerar as imagens PNG, utilize a seguinte linha de comando:

```bash
ffmpeg -f rawvideo -pix_fmt yuv420p -s 1280x720 -r 60 -i /home/gaci/videos/720p/FourPeople_1280x720_60.yuv -vf "fps=1" frame_%04d.png
```

### Explicação dos Parâmetros

- `-f rawvideo`: Trata a entrada como vídeo bruto.
- `-pix_fmt yuv420p`: Utiliza o formato de pixel YUV com subsampling de crominância 4:2:0.
- `-s 1280x720`: Define a resolução do vídeo de entrada como 1280x720.
- `-r 60`: Configura a taxa de quadros para 60 fps.
- `-i`: Especifica o arquivo de vídeo de entrada.
- `-vf "fps=1"`: Aplica um filtro para extrair um quadro por segundo.
- `frame_%04d.png`: Nomeia os arquivos de saída dos quadros extraídos.

## Executando o Script de Cálculo de SI e TI

Para calcular o SI e TI dos PNGs gerados, execute o script da seguinte maneira:

```bash
python3 calculate_siti_enhanced.py <frames_directory>
```

Substitua `<frames_directory>` pelo diretório onde os quadros PNG estão salvos.
```

A formatação acima utiliza Markdown para estruturar o texto, o que inclui cabeçalhos, blocos de código, e listas para tornar o conteúdo fácil de ler e seguir. Lembre-se de substituir `<frames_directory>` pelo diretório específico onde os quadros PNG estão armazenados, quando for utilizar o script.
