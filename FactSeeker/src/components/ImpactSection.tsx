import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { 
  Users, 
  Globe, 
  Shield, 
  ArrowRight,
  CheckCircle2
} from "lucide-react";

const stats = [
  {
    value: "70%",
    label: "of adults receive news via social media in India",
    icon: Users
  },
  {
    value: "3x",
    label: "faster than traditional fact-checking methods",
    icon: Shield
  },
  {
    value: "150+",
    label: "languages supported for global reach",
    icon: Globe
  }
];

const useCases = [
  {
    title: "Health Crises",
    description: "Detect false vaccine claims and treatments, send verified health advice instantly",
    icon: "🏥"
  },
  {
    title: "Political Events",
    description: "Identify misleading narratives during elections to prevent panic and manipulation",
    icon: "🗳️"
  },
  {
    title: "Public Safety",
    description: "Monitor disasters and festivals, alert citizens with verified emergency instructions",
    icon: "🚨"
  }
];

const ImpactSection = () => {
  return (
    <section className="py-24 px-4 bg-muted/30">
      <div className="container mx-auto max-w-7xl">
        {/* Section Header */}
        <div className="text-center mb-16 space-y-4">
          <h2 className="text-4xl md:text-5xl font-bold text-foreground">
            Real-World Impact
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Protecting communities and empowering individuals with accurate information
          </p>
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
          {stats.map((stat, index) => {
            const Icon = stat.icon;
            return (
              <Card 
                key={index}
                className="p-8 bg-gradient-card backdrop-blur-sm border-primary/10 text-center hover:shadow-glow transition-all duration-300"
              >
                <Icon className="w-12 h-12 text-primary mx-auto mb-4" />
                <div className="text-4xl md:text-5xl font-bold bg-gradient-primary bg-clip-text text-transparent mb-2">
                  {stat.value}
                </div>
                <p className="text-muted-foreground">{stat.label}</p>
              </Card>
            );
          })}
        </div>

        {/* Use Cases */}
        <div className="mb-16">
          <h3 className="text-3xl font-bold text-foreground text-center mb-12">
            Critical Use Cases
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {useCases.map((useCase, index) => (
              <Card 
                key={index}
                className="p-6 bg-gradient-card backdrop-blur-sm border-primary/10 hover:border-primary/30 transition-all duration-300 hover:-translate-y-1"
              >
                <div className="text-5xl mb-4">{useCase.icon}</div>
                <h4 className="text-xl font-semibold text-foreground mb-3">
                  {useCase.title}
                </h4>
                <p className="text-muted-foreground">
                  {useCase.description}
                </p>
              </Card>
            ))}
          </div>
        </div>

        {/* Differentiators */}
        <Card className="p-8 bg-gradient-card backdrop-blur-sm border-primary/10">
          <h3 className="text-2xl font-bold text-foreground mb-6 text-center">
            What Makes FactSeeker Different
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-4xl mx-auto">
            {[
              "Fully autonomous operation without manual triggers",
              "Multimodal intelligence across text, images, videos, and audio",
              "Explainable AI with transparent reasoning and sources",
              "Real-time impact scoring and prioritization",
              "Multi-agent coordination for parallel processing",
              "Predictive modeling for emerging trends"
            ].map((point, index) => (
              <div key={index} className="flex items-start gap-3">
                <CheckCircle2 className="w-5 h-5 text-success flex-shrink-0 mt-0.5" />
                <span className="text-muted-foreground">{point}</span>
              </div>
            ))}
          </div>
        </Card>

        {/* CTA */}
        <div className="mt-16 text-center">
          <Card className="p-12 bg-gradient-primary text-white shadow-glow">
            <h3 className="text-3xl font-bold mb-4">
              Ready to Combat Misinformation?
            </h3>
            <p className="text-lg opacity-90 mb-8 max-w-2xl mx-auto">
              Join us in building a safer, more informed digital society with AI-powered fact verification
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button variant="secondary" size="lg" className="gap-2">
                <Shield className="w-5 h-5" />
                Request Demo
              </Button>
              <Button 
                variant="outline" 
                size="lg" 
                className="bg-white/10 border-white/20 text-white hover:bg-white/20 gap-2"
              >
                View Documentation
                <ArrowRight className="w-5 h-5" />
              </Button>
            </div>
          </Card>
        </div>
      </div>
    </section>
  );
};

export default ImpactSection;
