import wamage1 from "../../assets/watch.png";
import shomage2 from "../../assets/sneakers.png";
import glage2 from "../../assets/glass.png";
import headage from "../../assets/headset.png";
import container from "../../assets/Container.png";
function Trending() {
  const props = [
    {
      title: "Architect Chrono V1",
      price: "$299.00",
      img: wamage1,
    },
    {
      title: "Velocity Runner",
      price: "$145.00",
      img: shomage2,
    },
    {
      title: "Eclipse Shade Pro",
      price: "$210.00",
      img: glage2,
    },
    {
      title: "Sonic Aura Wireless",
      price: "$349.00",
      img: headage,
    },
  ];
  return (
    <div>
      <p className="font-bold text-[12px] leading-[16px] tracking-[1.2px] text-[#006C46]  flex justify-center mt-[96px]">
        THE HOT LIST{" "}
      </p>
      <h1 className="font-black text-[48px] leading-[48px] tracking-[-2.4px] text-[#131B2E] flex justify-center pt-[8.5px] mb-[92px]">
        Trending Now
      </h1>
      <section className="grid grid-cols-4 gap-y-[32px] gap-x-[32px] pl-[32px] pr-[32px]">
        {props.map((item, index) => (
          <div
            key={index}
            className="cursor-pointer transition-all duration-300     hover:-translate-y-[5px] hover:shadow-lg"
          >
            <img
              src={item.img}
              alt={item.title}
              className="w-full h-[250px] object-cover rounded-xl"
            />
            <h2 className="mt-[16px] font-bold text-[18px] text-[#131B2E] leading-[28px]">
              {item.title}{" "}
            </h2>
            <p className="mt-[4px] text-[#6B7280] font-medium text-[16px] leading-[24px]">
              {" "}
              {item.price}{" "}
            </p>
          </div>
        ))}
      </section>
      {/* ....CARD...... */}
      <section className="bg-gradient-to-tr from-[#3132ED] to-[#5054FF]  h-[512px]  rounded-[24px] ml-[32px]  mr-[32px]  justify-between mt-[96px] mb-[96px] flex flex-row">
        {/* LEFT  HAND SIDE */}
        <div className=" flex flex-col  gap-[16px] p-[80px] pr-[px]">
             <p className="w-[426px] h-[120px] font-black leading-[60px] text-[#FFFFFF] text-[60px] ">20% Off Your First Order </p> 
             <p className="w-[426px] h-[100px] text-[#FFFFFF] font-normal text-[20px] leading-[28px]">Start your architectural journey today with an exclusive discount across our entire curated catalog.</p>
        </div>
        {/* RIGHT HAND SIDE */}
        <div className=""> <img src={container} alt="Container"  className=" pt-[40px] object-cover "/></div>
      </section>
    </div>
  );
}
export default Trending;
