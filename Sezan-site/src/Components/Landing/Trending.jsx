import wamage1 from "../../assets/watch.png"
import shomage2 from "../../assets/sneakers.png"
import glage2 from "../../assets/glass.png"
import headage from "../../assets/headset.png"
function Trending () {
    const props =[
        {
            title : "Architect Chrono V1"
            price : "$299.00"
            img : wamage1
        },
        {
            title:"Velocity Runner"
            price:"$145.00"
            img : shomage2
        },
        {
            title: "Eclipse Shade Pro"
            price :"$199.00"
            img : glage2  
        },
        
    ]
    return(
        <div>
            <p className="font-bold text-[12px] leading-[16px] tracking-[1.2px] text-[#006C46]  flex justify-center mt-[96px]">THE HOT LIST </p> 
            <h1 className="font-black text-[48px] leading-[48px] tracking-[-2.4px] text-[#131B2E] flex justify-center    pt-[8.5px]">Trending Now</h1>
        </div>
    )
}
export default Trending;