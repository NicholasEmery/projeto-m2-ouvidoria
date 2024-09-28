import { Component, OnInit } from '@angular/core';
import { DataService } from '../../data.service';

@Component({
  selector: 'table-root',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {

  manifestations: any[] = [];  // Armazena as manifestações
  selectedManifestation: any = null;  // Armazena a manifestação selecionada para edição

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.loadManifestations();
  }

  // Carrega todas as manifestações
  loadManifestations(): void {
    this.dataService.getManifestations().subscribe(data => {
      this.manifestations = data;
    });
  }

  // Abre o modal de criação
  openCreateModal(): void {
    this.selectedManifestation = { usuario: '', tipo: '', descricao: '' };  // Limpa a seleção para criar uma nova
  }

  // Abre o modal de edição
  openEditModal(manifestation: any): void {
    this.selectedManifestation = { ...manifestation };  // Clona os dados para editar
  }

  // Fecha o modal
  closeModal(): void {
    this.selectedManifestation = null;  // Fecha o modal limpando a seleção
  }

  // Deleta uma manifestação
  deleteManifestation(id: number): void {
    if (confirm('Tem certeza que deseja deletar?')) {
      this.dataService.deleteManifestation(id).subscribe(() => {
        this.loadManifestations();  // Atualiza a tabela
      });
    }
  }

  // Salva uma manifestação (tanto para criar quanto para editar)
  saveManifestation(manifestation: any): void {
    if (this.selectedManifestation?.id) {
      // Atualizar manifestação existente
      this.dataService.updateManifestation(this.selectedManifestation.id, manifestation).subscribe(() => {
        this.loadManifestations();  // Atualiza a tabela
      });
    } else {
      // Criar nova manifestação
      this.dataService.createManifestation(manifestation).subscribe(() => {
        this.loadManifestations();  // Atualiza a tabela
      });
    }
    this.closeModal();  // Fechar o modal após salvar
  }
}