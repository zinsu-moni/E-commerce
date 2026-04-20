import Navbar from "../Components/Navbar"
import Hero from "../Components/Hero"   
import Curated from "../Components/Landing/Curated"
import Trending from "../Components/Landing/Trending";
import Quote from "../Components/Landing/Quote";
function Landing (){
    return(
        <>
        <Navbar/>
        <Hero/>
        <Curated/>
        <Trending/>
        <Quote />
         <Fluid />
        </>

    )
}
export default Landing;