import Hero from "@/components/Hero";
import FeaturesSection from "@/components/FeaturesSection";
import DashboardPreview from "@/components/DashboardPreview";
import AgentVisualization from "@/components/AgentVisualization";
import ImpactSection from "@/components/ImpactSection";

const Index = () => {
  return (
    <div className="min-h-screen">
      <Hero />
      <FeaturesSection />
      <DashboardPreview />
      <AgentVisualization />
      <ImpactSection />
    </div>
  );
};

export default Index;
