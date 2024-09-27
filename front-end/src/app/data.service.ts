import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private apiUrl = 'http://localhost:5000/api/manifestacoes';  // API do backend

  constructor(private http: HttpClient) { }

  // Listar todas as manifestações
  getManifestations(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  // Criar uma nova manifestação
  createManifestation(data: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }

  // Editar uma manifestação existente
  updateManifestation(id: number, data: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${id}`, data);
  }

  // Deletar uma manifestação
  deleteManifestation(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${id}`);
  }
}
