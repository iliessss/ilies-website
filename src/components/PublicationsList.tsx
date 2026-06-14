"use client";

import { useMemo, useState } from "react";
import { t, type Locale } from "@/i18n/config";
import type { Dictionary } from "@/i18n/dictionary";
import type { Publication, PublicationType } from "@/content/site";
import { renderBold } from "@/lib/markup";

const typeLabelKey: Record<PublicationType, keyof Dictionary["publications"]> = {
  article: "typeArticle",
  preprint: "typePreprint",
  proceedings: "typeProceedings",
  thesis: "typeThesis",
};

const typeStyles: Record<PublicationType, string> = {
  article: "bg-accent-soft text-accent border-accent/30",
  preprint: "bg-amber-50 text-amber-700 border-amber-200 dark:bg-amber-950/40 dark:text-amber-300 dark:border-amber-900",
  proceedings: "bg-violet-50 text-violet-700 border-violet-200 dark:bg-violet-950/40 dark:text-violet-300 dark:border-violet-900",
  thesis: "bg-surface-2 text-muted border-border",
};

export default function PublicationsList({
  publications,
  locale,
  dict,
}: {
  publications: Publication[];
  locale: Locale;
  dict: Dictionary;
}) {
  const [filter, setFilter] = useState<PublicationType | "all">("all");

  // Types réellement présents, pour n'afficher que les filtres utiles
  const availableTypes = useMemo(() => {
    const set = new Set<PublicationType>();
    publications.forEach((p) => set.add(p.type));
    return Array.from(set);
  }, [publications]);

  const filtered = useMemo(
    () =>
      [...publications]
        .filter((p) => filter === "all" || p.type === filter)
        .sort((a, b) => b.year - a.year),
    [publications, filter],
  );

  const filterBtn = (active: boolean) =>
    active
      ? "rounded-full bg-accent px-3.5 py-1.5 text-sm font-medium text-white"
      : "rounded-full border border-border px-3.5 py-1.5 text-sm font-medium text-muted transition-colors hover:text-foreground hover:border-accent";

  return (
    <div>
      {availableTypes.length > 1 && (
        <div className="mt-8 flex flex-wrap gap-2">
          <button onClick={() => setFilter("all")} className={filterBtn(filter === "all")}>
            {dict.publications.filterAll}
          </button>
          {availableTypes.map((type) => (
            <button
              key={type}
              onClick={() => setFilter(type)}
              className={filterBtn(filter === type)}
            >
              {dict.publications[typeLabelKey[type]]}
            </button>
          ))}
        </div>
      )}

      <ol className="mt-8 space-y-6">
        {filtered.map((pub, i) => (
          <li
            key={i}
            className="rounded-xl border border-border bg-surface p-5 transition-colors hover:border-accent/50"
          >
            <div className="flex flex-wrap items-center gap-2.5">
              <span
                className={`inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-medium ${typeStyles[pub.type]}`}
              >
                {dict.publications[typeLabelKey[pub.type]]}
              </span>
              <span className="font-mono text-sm text-muted-2">{pub.year}</span>
            </div>

            <h3 className="mt-2.5 font-serif text-lg font-semibold leading-snug text-foreground">
              {t(pub.title, locale)}
            </h3>
            <p className="mt-1.5 text-sm text-muted">{renderBold(pub.authors)}</p>
            <p className="text-sm italic text-muted-2">{t(pub.venue, locale)}</p>

            {pub.abstract && (
              <details className="group mt-3">
                <summary className="cursor-pointer text-sm font-medium text-accent marker:content-none">
                  {dict.publications.abstract} +
                </summary>
                <p className="mt-2 text-sm leading-relaxed text-muted">
                  {t(pub.abstract, locale)}
                </p>
              </details>
            )}

            {pub.links && Object.values(pub.links).some(Boolean) && (
              <div className="mt-4 flex flex-wrap gap-2">
                {pub.links.pdf && <LinkPill href={pub.links.pdf} label="PDF" />}
                {pub.links.doi && <LinkPill href={pub.links.doi} label="DOI" />}
                {pub.links.arxiv && <LinkPill href={pub.links.arxiv} label="arXiv" />}
                {pub.links.hal && <LinkPill href={pub.links.hal} label="HAL" />}
                {pub.links.code && <LinkPill href={pub.links.code} label="Code" />}
              </div>
            )}
          </li>
        ))}
      </ol>
    </div>
  );
}

function LinkPill({ href, label }: { href: string; label: string }) {
  return (
    <a
      href={href}
      target="_blank"
      rel="noopener noreferrer"
      className="inline-flex items-center rounded-md border border-border px-2.5 py-1 text-xs font-semibold text-muted transition-colors hover:border-accent hover:text-accent"
    >
      {label}
    </a>
  );
}
