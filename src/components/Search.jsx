import {useState} from "react";

export default function Search(){
    const [value, setValue] = useState('');
    const buscar = (e) => setValue(e.target.value)
    return (
        <div>
            <center>
                <h1 class="mt-5">Search Movie</h1>
                <h2>{value}</h2>
                <form action={"/detail/"+value} method="POST">
                    <input type="search" class="form-control p-3" value={value} onChange={buscar} 
                    placeholder="Search"/>
                </form>
            </center>
        </div>
    )
}
