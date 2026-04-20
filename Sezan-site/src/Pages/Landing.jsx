import Navbar from "../Components/Navbar"
import Hero from "../Components/Hero"   
import Curated from "../Components/Landing/Curated"
import Trending from "../Components/Landing/Trending";
import Quote from "../Components/Landing/Quote";
import Fluid from "../Components/Landing/Fluid";
import Footer from "../Components/Landing/Footer";
function Landing (){
    return(
        <>
        <Navbar/>
        <Hero/>
        <Curated/>
        <Trending/>
        <Quote />
            <Fluid />
            <Footer />
        </>

    )
}
export default Landing;