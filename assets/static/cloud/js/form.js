const App = ()=>{
    const {useState} = React;
    const [step,setStep] = useState(0);
    const [hideButton,setHideButton] = useState(0);
    
    const step_form = step+1;
    
    const Form = ()=>{
    
    if(step==0){
    
    return (
    <Login /> );
    
    }else if(step==1){
    
    return (
    <Contact /> );
    
    }else if(step==2){
    
    return (
    <Social /> );
    
    }else if(step==3){
    
    return (
    <Welcome /> );
    }
    }
    const Login = () =>{
    
    return (
    <>
        <div className="form_body">
            <div className="header">
                <h1>Basic Details</h1>
                <span>{step_form}</span>
            </div>
            <div className="form_data">
                <div className="input_field">
                    <input type="text" required />
                    <span>Name</span>
                </div>
    
                <div className="input_field">
                    <input type="text" required />
                    <span>Email</span>
                </div>
    
                <div className="input_field">
                    <input type="text" required />
                    <span>Password</span>
                </div>
    
                <div className="input_field">
                    <input type="password" required />
                    <span>Repeat password</span>
                </div>
            </div>
        </div>
        <div className="footer">
            <button onClick={()=>{setStep(step+1)}}>Next</button>
        </div>
    </>
    );
    }
    
    
    const Contact = () =>{
    
    return (
    <>
        <div className="form_body">
            <div className="header">
                <h1>Contact Info</h1>
                <span>{step_form}</span>
            </div>
            <div className="form_data">
                <div className="input_field">
                    <input type="text" required />
                    <span>Country</span>
                </div>
    
                <div className="input_field">
                    <input type="text" required />
                    <span>State</span>
                </div>
    
                <div className="input_field">
                    <input type="text" required />
                    <span>Address Line 1</span>
                </div>
    
                <div className="input_field">
                    <input type="text" required />
                    <span>Address Line 2</span>
                </div>
            </div>
        </div>
        <div className="footer">
            <button onClick={()=>{setStep(step-1)}}>Previous</button>
            <button onClick={()=>{setStep(step+1)}}>Next</button>
        </div>
    </>
    );
    }
    
    
    const Social = () =>{
    
    return (
    <>
        <div className="form_body">
            <div className="header">
                <h1>Social Info</h1>
                <span>{step_form}</span>
            </div>
            <div className="form_data">
                <div className="input_field">
                    <input type="text" required />
                    <span>Facebook</span>
                </div>
    
                <div className="input_field">
                    <input type="text" required />
                    <span>Instgram</span>
                </div>
    
                <div className="input_field">
                    <input type="text" required />
                    <span>Linkedin</span>
                </div>
    
                <div className="input_field">
                    <input type="text" required />
                    <span>Twitter</span>
                </div>
            </div>
        </div>
        <div className="footer">
            <button onClick={()=>{setStep(step-1)}}>Previous</button>
            <button onClick={()=>{setStep(step+1)}}>Finish</button>
        </div>
    </>
    );
    }
    
    
    const Welcome = () =>{
    
    return (
    <>
        <div className="final">
            <div className="final_content">
                <span className="check"><i className="fa fa-check"></i></span>
                <p>Your Information has been submitted! We will contact you soon!</p>
            </div>
        </div>
    </>
    );
    }
    
    
    
    
    return (
    
    <>
        <div class="form">
            <div className="card">
                <div>{
                    <Form />}</div>
    
            </div>
        </div>
    </>
    );
    
    }
    
    ReactDOM.render(
    <App />,document.getElementById("root"));