import { Card } from "@/components/ui/card";
import { 
  Brain, 
  Eye, 
  Shield, 
  Zap, 
  MessageSquare, 
  TrendingUp,
  Database,
  Users
} from "lucide-react";

const features = [
  {
    icon: Brain,
    title: "Multi-Agent Architecture",
    description: "Specialized AI agents working autonomously to detect, verify, and alert about misinformation in real-time.",
    color: "text-primary"
  },
  {
    icon: Eye,
    title: "Multimodal Analysis",
    description: "Analyzes text, images, videos, and audio across social media, news outlets, and messaging platforms.",
    color: "text-secondary"
  },
  {
    icon: Shield,
    title: "RAG Verification",
    description: "Retrieves verified information from trusted sources like WHO, government portals, and fact-checking sites.",
    color: "text-success"
  },
  {
    icon: Zap,
    title: "Real-Time Alerts",
    description: "Instant notifications via WhatsApp, Telegram, and web dashboards with actionable verified information.",
    color: "text-warning"
  },
  {
    icon: MessageSquare,
    title: "Explainable AI",
    description: "Transparent reasoning showing why content was flagged, sources referenced, and confidence scores.",
    color: "text-accent"
  },
  {
    icon: TrendingUp,
    title: "Predictive Analysis",
    description: "Anticipates potential misinformation trends before they go viral using social network analysis.",
    color: "text-primary"
  },
  {
    icon: Database,
    title: "Impact Scoring",
    description: "Prioritizes high-risk misinformation based on virality potential, source credibility, and severity.",
    color: "text-secondary"
  },
  {
    icon: Users,
    title: "Community Engagement",
    description: "Users provide feedback, contribute to model training, and report new misinformation sources.",
    color: "text-success"
  }
];

const FeaturesSection = () => {
  return (
    <section className="py-24 px-4 bg-background">
      <div className="container mx-auto max-w-7xl">
        {/* Section Header */}
        <div className="text-center mb-16 space-y-4">
          <h2 className="text-4xl md:text-5xl font-bold text-foreground">
            Powerful Features
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Leveraging cutting-edge AI technologies to combat misinformation at scale
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {features.map((feature, index) => {
            const Icon = feature.icon;
            return (
              <Card 
                key={index}
                className="p-6 bg-gradient-card backdrop-blur-sm border-primary/10 hover:border-primary/30 transition-all duration-300 hover:shadow-glow hover:-translate-y-1"
              >
                <div className="space-y-4">
                  <div className={`w-12 h-12 rounded-lg bg-gradient-primary flex items-center justify-center ${feature.color}`}>
                    <Icon className="w-6 h-6 text-white" />
                  </div>
                  <h3 className="text-xl font-semibold text-foreground">
                    {feature.title}
                  </h3>
                  <p className="text-muted-foreground">
                    {feature.description}
                  </p>
                </div>
              </Card>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default FeaturesSection;
