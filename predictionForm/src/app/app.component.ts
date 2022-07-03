import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { PredictionServiceService } from './Service/prediction-service.service';
import { NgxSpinnerService } from "ngx-spinner";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'predictionForm';
  predictionForm = new FormGroup({
    swt: new FormControl(false, { validators: [Validators.required]}),
    diffBr: new FormControl(false, { validators: [Validators.required]}),
    chestPn: new FormControl(false, { validators: [Validators.required]}),
    abCramp: new FormControl(false, { validators: [Validators.required]}),
    headache: new FormControl(false, { validators: [Validators.required]}),
    dizz: new FormControl(false, { validators: [Validators.required]}),
    fear: new FormControl(false, { validators: [Validators.required]}),
    depres: new FormControl(false, { validators: [Validators.required]}),
    flashbk: new FormControl(false, { validators: [Validators.required]}),
    trem: new FormControl(false, { validators: [Validators.required]}),
    bluVi: new FormControl(false, { validators: [Validators.required]}),
    tunVi: new FormControl(false, { validators: [Validators.required]}),
    senTer: new FormControl(false, { validators: [Validators.required]}),
    firstYes: new FormControl(false, { validators: [Validators.required]}),
    lastYes: new FormControl(false, { validators: [Validators.required]}),
  });

  isLoading: boolean = true;
  formData: any;
  prediction: any;
  precentage: any;
  color: string | undefined;

  constructor(private predictionServiceService: PredictionServiceService, private spinner: NgxSpinnerService) { }

  ngOnInit(): void {
    this.isLoading = false;
  }
  onSubmit(){
    this.spinner.show();
    this.formData = this.predictionForm.value;
    let formData = new FormData();
    formData.append("swt", this.formData.swt);
    formData.append("diffBr" , this.formData.diffBr);
    formData.append("chestPn" , this.formData.chestPn);
    formData.append("abCramp" , this.formData.abCramp);
    formData.append("headache" , this.formData.headache);
    formData.append("dizz" , this.formData.dizz);
    formData.append("fear" , this.formData.fear);
    formData.append("depres" , this.formData.depres);
    formData.append("flashbk" , this.formData.flashbk);
    formData.append("trem" , this.formData.trem);
    formData.append("bluVi" , this.formData.bluVi);
    formData.append("tunVi" , this.formData.tunVi);
    formData.append("senTer" , this.formData.senTer);
    formData.append("firstYes" , this.formData.firstYes);
    formData.append("lastYes" , this.formData.lastYes);

    this.predictionServiceService.PostPredictionForm(this.formData).subscribe({
      next: (response) => {
        this.prediction = response;
        this.spinner.hide();
        if(response){
          switch (response) {
            case "low":
              this.color = "green";
              this.precentage = 30;
              break;
            case "mid":
              this.color = "yellow";
              this.precentage = 60;
              break;
            case "high":
              this.color = "red";
              this.precentage = 90;
              break;

            default:
              break;
          }
        }
      },
      error: (error) => console.log(error),
    });;
  }
}
