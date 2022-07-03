import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

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

  ngOnInit(): void {
    this.isLoading = false;
  }
  onSubmit(){
    this.formData = this.predictionForm.getRawValue();
  }
}
