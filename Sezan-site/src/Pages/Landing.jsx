import Navbar from "../Components/Navbar"
import Hero from "../Components/Hero"   
import Curated from "../Components/Landing/Curated"
import Trending from "../Components/Landing/Trending";
function Landing (){
    return(
        <>
        <Navbar/>
        <Hero/>
        <Curated/>
        <Trending/>
        </>
    )
}
export default Landing;