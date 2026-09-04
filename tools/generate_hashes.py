#!/usr/bin/env python3
"""
Sunsix Linux - Ferramenta de Catalogação e Hash do Sistema de Arquivos

Este script percorre uma pasta descompactada do `filesystem.squashfs` ou da ISO
e gera um índice de somas de verificação SHA-256 para todos os arquivos.

Uso:
    python generate_hashes.py /caminho/para/squashfs-extracted -o sunsix_hashes.csv
"""

import os
import sys
import hashlib
import argparse

def compute_sha256(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(65536):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        return f"ERROR: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Gera hashes SHA-256 para arquivos de uma pasta descompactada.")
    parser.add_argument("directory", help="Diretório raiz para analisar (ex: squashfs-root)")
    parser.add_argument("-o", "--output", default="file_hashes.csv", help="Arquivo CSV de saída (padrão: file_hashes.csv)")
    
    args = parser.parse_args()
    
    target_dir = os.path.abspath(args.directory)
    if not os.path.isdir(target_dir):
        print(f"Erro: {target_dir} não é um diretório válido.")
        sys.exit(1)

    print(f"🔬 Analisando diretório: {target_dir}")
    print(f"💾 Salvando em: {args.output}")

    count = 0
    with open(args.output, 'w', encoding='utf-8') as out_f:
        out_f.write("rel_path,sha256,size_bytes\n")
        
        for root, _, files in os.walk(target_dir):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, target_dir).replace("\\", "/")
                
                try:
                    file_size = os.path.getsize(abs_path)
                except OSError:
                    file_size = 0
                    
                sha256_hash = compute_sha256(abs_path)
                out_f.write(f'"{rel_path}","{sha256_hash}",{file_size}\n')
                count += 1
                
                if count % 1000 == 0:
                    print(f"  ... {count} arquivos processados")

    print(f"✅ Concluído! Total de arquivos catalogados: {count}")

if __name__ == "__main__":
    main()
