import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PredictionServiceService {
  BASE_URL = "http://127.0.0.1:5000/"

  constructor(private http: HttpClient) { }

  PostPredictionForm(formData:FormData){
    return this.http.post(this.BASE_URL + 'getFinalPrediction', formData);
  }
}
