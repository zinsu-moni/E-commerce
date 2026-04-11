import { Link } from "react-router-dom";
import arrow from "../assets/arrow.svg";
import hero from "../assets/image.png"
function Hero (){
    return(
        <div className="flex flex-row justify-between"> 
           <section className="pl-[40px] mt-[70px]">
             <h1 className="w-[308px] text-8xl h-[102.5px] font-normal leading-[96px] tracking-[4.8px]">Redefining</h1>
             <h1 className="w-[308px] text-8xl  h-[102.5px] text-[#3132ED] italic text-[96px] font-normal leading-[96px]  tracking-[0px]">Digital</h1>
             <h1 className="w-[308px] text-8xl h-[102.5px] font-normal leading-[96px] tracking-[4.8px]">Commerce</h1>
             <p className="w-[576px] h-[84px] text-xl tracking-[1px] leading-[1.2] text-[#64748B] mt-[20px] mb-[20px] font-normal">Experience the future of fluid shopping. We blend <br />arhitectural precision with liquid editorial  deign to curate <br />the world's most sought-after essentials  </p>
               <div className="flex flex-row gap-4">
                <Link to = "./ "><button className="bg-gradient-to-r from-[#3132ED] to-[#5054FF] text-white  rounded-[8px]  w-[184px] h-[56px]         justify-center items-center hover:bg-red-500 transition duration-300 flex flex-row items-center gap-2 shadow-md"> <span>Shop Now</span><img src={arrow} alt="" /></button></Link>
                <Link to = "./"><button className="bg-[#FFFFFF] text-[#3132ED] w-[184px] h-[56px] justify-center items-center font-medium hover:bg-red-500 transition duration-300 flex flex-row items-center gap-2 shadow-md"> <span>Browse site</span></button></Link>
              </div>
            </section>
           <div>  <Link><img src={hero} alt="" className="object-cover w-[485px] h-[620px] mt-[30px]" /></Link></div> 
        </div>
    )
}
export default Hero;