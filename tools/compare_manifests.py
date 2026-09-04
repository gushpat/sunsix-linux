#!/usr/bin/env python3
"""
Sunsix Linux - Ferramenta de Comparação de Manifestos de Pacotes

Este script compara dois arquivos de manifesto de pacotes (formato .manifest do Ubiquity/Casper
ou saídas de `dpkg-query -W -f='${Package}\t${Version}\n'`) para identificar diferenças
entre a distribuição Sunsix Linux e a imagem de referência Ubuntu Stock.

Uso:
    python compare_manifests.py sunsix.manifest ubuntu.manifest
"""

import sys
import os

def load_manifest(filepath):
    packages = {}
    if not os.path.exists(filepath):
        print(f"Erro: Arquivo {filepath} não encontrado.")
        sys.exit(1)
        
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split()
            if len(parts) >= 2:
                pkg_name = parts[0]
                pkg_version = parts[1]
                packages[pkg_name] = pkg_version
            elif len(parts) == 1:
                packages[parts[0]] = "desconhecido"
    return packages

def generate_markdown_report(sunsix_pkgs, ubuntu_pkgs, sunsix_file, ubuntu_file):
    sunsix_keys = set(sunsix_pkgs.keys())
    ubuntu_keys = set(ubuntu_pkgs.keys())
    
    common = sunsix_keys & ubuntu_keys
    only_sunsix = sunsix_keys - ubuntu_keys
    only_ubuntu = ubuntu_keys - sunsix_keys
    
    version_mismatches = {}
    for pkg in common:
        if sunsix_pkgs[pkg] != ubuntu_pkgs[pkg]:
            version_mismatches[pkg] = (sunsix_pkgs[pkg], ubuntu_pkgs[pkg])

    report = []
    report.append(f"# 📊 Relatório de Comparação de Pacotes")
    report.append(f"**Mídia A (Sunsix):** `{sunsix_file}` ({len(sunsix_pkgs)} pacotes)")
    report.append(f"**Mídia B (Ubuntu):** `{ubuntu_file}` ({len(ubuntu_pkgs)} pacotes)\n")
    
    report.append(f"## 📈 Resumo Estatístico")
    report.append(f"- **Pacotes em Comum:** {len(common)}")
    report.append(f"- **Diferenças de Versão:** {len(version_mismatches)}")
    report.append(f"- **Exclusivos do Sunsix:** {len(only_sunsix)}")
    report.append(f"- **Ausentes no Sunsix (Só no Ubuntu):** {len(only_ubuntu)}\n")
    
    if only_sunsix:
        report.append(f"## 🟡 Pacotes Exclusivos do Sunsix ({len(only_sunsix)})")
        report.append("| Pacote | Versão Sunsix |")
        report.append("| :--- | :--- |")
        for pkg in sorted(only_sunsix):
            report.append(f"| `{pkg}` | `{sunsix_pkgs[pkg]}` |")
        report.append("")

    if version_mismatches:
        report.append(f"## ⚠️ Diferenças de Versão ({len(version_mismatches)})")
        report.append("| Pacote | Versão Sunsix | Versão Ubuntu Stock |")
        report.append("| :--- | :--- | :--- |")
        for pkg in sorted(version_mismatches.keys()):
            v_sun, v_ubu = version_mismatches[pkg]
            report.append(f"| `{pkg}` | `{v_sun}` | `{v_ubu}` |")
        report.append("")

    return "\n".join(report)

def main():
    if len(sys.argv) < 3:
        print("Uso: python compare_manifests.py <sunsix.manifest> <ubuntu.manifest>")
        print("Exemplo: python compare_manifests.py casper_sunsix.manifest casper_ubuntu.manifest")
        sys.exit(1)
        
    sunsix_file = sys.argv[1]
    ubuntu_file = sys.argv[2]
    
    sunsix_pkgs = load_manifest(sunsix_file)
    ubuntu_pkgs = load_manifest(ubuntu_file)
    
    report = generate_markdown_report(sunsix_pkgs, ubuntu_pkgs, sunsix_file, ubuntu_file)
    print(report)

if __name__ == "__main__":
    main()
